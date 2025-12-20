"""Specialized subagents for the multi-agent RAG chatbot system."""

from typing import List, Dict, Optional, Tuple
import logging
from openai import OpenAI
from config import settings
from agent_skills import search_module_content, find_code_examples, get_prerequisites, explain_concept

logger = logging.getLogger(__name__)


class Agent:
    """Base Agent class for specialized subagents."""

    def __init__(self, name: str, expertise: List[str], instructions: str):
        self.name = name
        self.expertise = expertise
        self.instructions = instructions
        # Initialize the OpenAI client with Gemini via OpenAI SDK
        self.client = OpenAI(
            api_key=settings.gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """Process a query using the agent's specialized knowledge."""
        raise NotImplementedError("Subclasses must implement process_query method")


class ROS2Agent(Agent):
    """Specialized agent for ROS 2 related queries."""

    def __init__(self):
        expertise = ["ROS 2", "nodes", "topics", "services", "URDF", "TF2", "rclpy", "launch files", "actions"]
        instructions = """
        You are ROS2Expert, specializing in Module 1: The Robotic Nervous System.

        Your expertise: ROS 2 architecture, nodes, topics, services, actions, URDF,
        TF2 transforms, rclpy, launch files, robot description formats.

        When answering:
        1. Use search_module_content('module-1-ros2', query)
        2. Provide ROS 2 specific examples
        3. Reference ROS 2 commands and concepts
        4. Use find_code_examples() for code snippets

        Answer based ONLY on retrieved module content.
        """
        super().__init__("ROS2Expert", expertise, instructions)

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """Process a ROS 2 related query."""
        try:
            # Use the specialized search for module 1 content
            context_docs = search_module_content("module-1-ros2", question)

            # Build the context from retrieved documents
            context_str = "\n".join([f"Context {i+1}: {doc['text'][:500]}..." for i, doc in enumerate(context_docs[:3])])

            # Build the prompt based on whether selected text is provided
            if selected_text:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                User has selected text: {selected_text}

                Question: {question}

                Answer the question thoroughly, focusing on the selected text and using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include ROS 2 specific examples and commands where relevant.
                """
            else:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                Question: {question}

                Answer the question thoroughly using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include ROS 2 specific examples and commands where relevant.
                """

            # Call the OpenAI-compatible API (Gemini)
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.temperature,
                max_tokens=800
            )

            # Extract the answer from the response
            if response and hasattr(response, 'choices') and response.choices:
                choice = response.choices[0]
                if choice and hasattr(choice, 'message') and choice.message:
                    answer = choice.message.content if hasattr(choice.message, 'content') else "I don't have information about that in the book."
                else:
                    answer = "I don't have information about that in the book."
            else:
                answer = "I don't have information about that in the book."

            # Format the sources from the retrieved documents using real metadata
            sources = []
            for i, doc in enumerate(context_docs):
                source = {
                    "url": doc.get("url", ""),
                    "title": doc.get("title", f"ROS 2 Content {i+1}"),
                    "content": doc["text"][:200] + "..." if len(doc["text"]) > 200 else doc["text"],
                    "score": doc.get("score", 1.0)
                }
                sources.append(source)

            return answer, sources

        except Exception as e:
            logger.error(f"Error in ROS2Agent: {str(e)}")
            return "I encountered an error processing your ROS 2 question.", []


class SimulationAgent(Agent):
    """Specialized agent for simulation related queries."""

    def __init__(self):
        expertise = ["Gazebo", "Unity", "physics simulation", "URDF/SDF", "sensors", "sim-to-real"]
        instructions = """
        You are SimulationExpert, specializing in Module 2: The Digital Twin.

        Your expertise: Gazebo simulation, Unity integration, physics engines,
        URDF/SDF formats, sensor simulation, sim-to-real transfer.

        When answering:
        1. Use search_module_content('module-2-simulation', query)
        2. Explain simulation concepts clearly
        3. Reference Gazebo and Unity specifics
        4. Use find_code_examples() for configuration files

        Answer based ONLY on retrieved module content.
        """
        super().__init__("SimulationExpert", expertise, instructions)

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """Process a simulation related query."""
        try:
            # Use the specialized search for module 2 content
            context_docs = search_module_content("module-2-simulation", question)

            # Build the context from retrieved documents
            context_str = "\n".join([f"Context {i+1}: {doc['text'][:500]}..." for i, doc in enumerate(context_docs[:3])])

            # Build the prompt based on whether selected text is provided
            if selected_text:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                User has selected text: {selected_text}

                Question: {question}

                Answer the question thoroughly, focusing on the selected text and using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include simulation-specific examples and configuration details where relevant.
                """
            else:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                Question: {question}

                Answer the question thoroughly using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include simulation-specific examples and configuration details where relevant.
                """

            # Call the OpenAI-compatible API (Gemini)
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.temperature,
                max_tokens=800
            )

            # Extract the answer from the response
            if response and hasattr(response, 'choices') and response.choices:
                choice = response.choices[0]
                if choice and hasattr(choice, 'message') and choice.message:
                    answer = choice.message.content if hasattr(choice.message, 'content') else "I don't have information about that in the book."
                else:
                    answer = "I don't have information about that in the book."
            else:
                answer = "I don't have information about that in the book."

            # Format the sources from the retrieved documents using real metadata
            sources = []
            for i, doc in enumerate(context_docs):
                source = {
                    "url": doc.get("url", ""),
                    "title": doc.get("title", f"Simulation Content {i+1}"),
                    "content": doc["text"][:200] + "..." if len(doc["text"]) > 200 else doc["text"],
                    "score": doc.get("score", 1.0)
                }
                sources.append(source)

            return answer, sources

        except Exception as e:
            logger.error(f"Error in SimulationAgent: {str(e)}")
            return "I encountered an error processing your simulation question.", []


class IsaacAgent(Agent):
    """Specialized agent for Isaac related queries."""

    def __init__(self):
        expertise = ["Isaac Sim", "VSLAM", "Nav2", "synthetic data", "perception", "NVIDIA Isaac"]
        instructions = """
        You are IsaacExpert, specializing in Module 3: The AI-Robot Brain.

        Your expertise: NVIDIA Isaac Sim, Isaac ROS, VSLAM, Nav2, synthetic data,
        perception pipelines, GPU acceleration, sim-to-real deployment.

        When answering:
        1. Use search_module_content('module-3-isaac', query)
        2. Explain NVIDIA Isaac concepts
        3. Reference perception and navigation systems
        4. Use find_code_examples() for Isaac code

        Answer based ONLY on retrieved module content.
        """
        super().__init__("IsaacExpert", expertise, instructions)

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """Process an Isaac related query."""
        try:
            # Use the specialized search for module 3 content
            context_docs = search_module_content("module-3-isaac", question)

            # Build the context from retrieved documents
            context_str = "\n".join([f"Context {i+1}: {doc['text'][:500]}..." for i, doc in enumerate(context_docs[:3])])

            # Build the prompt based on whether selected text is provided
            if selected_text:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                User has selected text: {selected_text}

                Question: {question}

                Answer the question thoroughly, focusing on the selected text and using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include Isaac-specific examples and code where relevant.
                """
            else:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                Question: {question}

                Answer the question thoroughly using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include Isaac-specific examples and code where relevant.
                """

            # Call the OpenAI-compatible API (Gemini)
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.temperature,
                max_tokens=800
            )

            # Extract the answer from the response
            if response and hasattr(response, 'choices') and response.choices:
                choice = response.choices[0]
                if choice and hasattr(choice, 'message') and choice.message:
                    answer = choice.message.content if hasattr(choice.message, 'content') else "I don't have information about that in the book."
                else:
                    answer = "I don't have information about that in the book."
            else:
                answer = "I don't have information about that in the book."

            # Format the sources from the retrieved documents using real metadata
            sources = []
            for i, doc in enumerate(context_docs):
                source = {
                    "url": doc.get("url", ""),
                    "title": doc.get("title", f"Isaac Content {i+1}"),
                    "content": doc["text"][:200] + "..." if len(doc["text"]) > 200 else doc["text"],
                    "score": doc.get("score", 1.0)
                }
                sources.append(source)

            return answer, sources

        except Exception as e:
            logger.error(f"Error in IsaacAgent: {str(e)}")
            return "I encountered an error processing your Isaac question.", []


class VLAAgent(Agent):
    """Specialized agent for Vision-Language-Action related queries."""

    def __init__(self):
        expertise = ["Whisper", "LLMs", "voice control", "vision-language-action", "GPT-4", "multimodal AI"]
        instructions = """
        You are VLAExpert, specializing in Module 4: Vision-Language-Action.

        Your expertise: OpenAI Whisper, LLM integration, GPT-4, voice commands,
        vision-language models, multimodal AI, natural language robot control.

        When answering:
        1. Use search_module_content('module-4-vla', query)
        2. Explain VLA concepts and architecture
        3. Reference voice and language integration
        4. Use find_code_examples() for LLM code

        Answer based ONLY on retrieved module content.
        """
        super().__init__("VLAExpert", expertise, instructions)

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict]]:
        """Process a VLA related query."""
        try:
            # Use the specialized search for module 4 content
            context_docs = search_module_content("module-4-vla", question)

            # Build the context from retrieved documents
            context_str = "\n".join([f"Context {i+1}: {doc['text'][:500]}..." for i, doc in enumerate(context_docs[:3])])

            # Build the prompt based on whether selected text is provided
            if selected_text:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                User has selected text: {selected_text}

                Question: {question}

                Answer the question thoroughly, focusing on the selected text and using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include VLA-specific examples and architecture details where relevant.
                """
            else:
                system_prompt = f"""
                {self.instructions}

                Retrieved content for context:
                {context_str}
                """

                user_prompt = f"""
                Question: {question}

                Answer the question thoroughly using the retrieved content as context. Provide detailed explanations in complete sentences without unnecessary repetition. Include VLA-specific examples and architecture details where relevant.
                """

            # Call the OpenAI-compatible API (Gemini)
            response = self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=settings.temperature,
                max_tokens=800
            )

            # Extract the answer from the response
            if response and hasattr(response, 'choices') and response.choices:
                choice = response.choices[0]
                if choice and hasattr(choice, 'message') and choice.message:
                    answer = choice.message.content if hasattr(choice.message, 'content') else "I don't have information about that in the book."
                else:
                    answer = "I don't have information about that in the book."
            else:
                answer = "I don't have information about that in the book."

            # Format the sources from the retrieved documents using real metadata
            sources = []
            for i, doc in enumerate(context_docs):
                source = {
                    "url": doc.get("url", ""),
                    "title": doc.get("title", f"VLA Content {i+1}"),
                    "content": doc["text"][:200] + "..." if len(doc["text"]) > 200 else doc["text"],
                    "score": doc.get("score", 1.0)
                }
                sources.append(source)

            return answer, sources

        except Exception as e:
            logger.error(f"Error in VLAAgent: {str(e)}")
            return "I encountered an error processing your VLA question.", []


class CoordinatorAgent:
    """Main agent that analyzes questions and routes to appropriate subagent."""

    def __init__(self):
        self.ros2_agent = ROS2Agent()
        self.simulation_agent = SimulationAgent()
        self.isaac_agent = IsaacAgent()
        self.vla_agent = VLAAgent()

        # Keyword mappings for routing
        self.keyword_mapping = {
            'ros2': ['ros', 'ros2', 'node', 'topic', 'service', 'urdf', 'tf2', 'rclpy', 'launch', 'action', 'rosbag'],
            'simulation': ['gazebo', 'unity', 'simulation', 'physics', 'sdf', 'simulator', 'sim-to-real', 'digital twin'],
            'isaac': ['isaac', 'vslam', 'nav2', 'synthetic', 'perception', 'nvidia', 'isaac sim', 'isaac_ros'],
            'vla': ['voice', 'whisper', 'llm', 'gpt', 'language', 'vision-language', 'vla', 'multimodal', 'cognitive']
        }

    def route_to_subagent(self, question: str) -> Agent:
        """Route the question to the appropriate subagent based on keywords."""
        question_lower = question.lower()

        # Count keyword matches for each agent
        scores = {
            'ros2': 0,
            'simulation': 0,
            'isaac': 0,
            'vla': 0
        }

        for category, keywords in self.keyword_mapping.items():
            for keyword in keywords:
                if keyword in question_lower:
                    scores[category] += 1

        # Find the category with the highest score
        best_category = max(scores, key=scores.get)

        # Return the appropriate agent based on the best category
        if scores[best_category] > 0:
            if best_category == 'ros2':
                return self.ros2_agent
            elif best_category == 'simulation':
                return self.simulation_agent
            elif best_category == 'isaac':
                return self.isaac_agent
            elif best_category == 'vla':
                return self.vla_agent
        else:
            # Default to ROS2 agent if no keywords match (most fundamental)
            return self.ros2_agent

    def process_query(self, question: str, selected_text: Optional[str] = None) -> Tuple[str, List[Dict], str]:
        """Process a query by routing to the appropriate subagent."""
        # Route to the appropriate subagent
        subagent = self.route_to_subagent(question)

        # Process the query with the selected subagent
        answer, sources = subagent.process_query(question, selected_text)

        # Return answer, sources, and the subagent used for transparency
        return answer, sources, subagent.name