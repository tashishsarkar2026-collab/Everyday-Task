<mxfile host="app.diagrams.net">
  <diagram name="Architecture">
    <mxGraphModel dx="1420" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Top Header -->
        <mxCell id="header" value="Enterprise Security, Observability &amp; Governance"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=16;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="20" y="20" width="1200" height="60" as="geometry"/>
        </mxCell>

        <!-- Input Layer -->
        <mxCell id="input" value="Input Layer&#xa;(External Systems)"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;"
          vertex="1" parent="1">
          <mxGeometry x="20" y="120" width="160" height="300" as="geometry"/>
        </mxCell>

        <!-- Secure Ingestion -->
        <mxCell id="ingestion" value="Secure Ingestion Gateway (FastAPI)&#xa;- Azure AD Auth&#xa;- File Type Validation&#xa;- File Size Validation&#xa;- Schema Validation"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;"
          vertex="1" parent="1">
          <mxGeometry x="200" y="120" width="200" height="300" as="geometry"/>
        </mxCell>

        <!-- Content Security -->
        <mxCell id="content" value="Content Security Layer&#xa;- Blob Storage&#xa;- Defender Scan&#xa;- Reject/Quarantine"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;"
          vertex="1" parent="1">
          <mxGeometry x="420" y="120" width="200" height="300" as="geometry"/>
        </mxCell>

        <!-- Messaging -->
        <mxCell id="messaging" value="Messaging Layer&#xa;- Azure Service Bus&#xa;- Async Processing"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;"
          vertex="1" parent="1">
          <mxGeometry x="640" y="120" width="200" height="300" as="geometry"/>
        </mxCell>

        <!-- Processing -->
        <mxCell id="processing" value="Processing Layer&#xa;- Azure Document Intelligence&#xa;- OCR + Text Extraction"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;"
          vertex="1" parent="1">
          <mxGeometry x="860" y="120" width="220" height="300" as="geometry"/>
        </mxCell>

        <!-- AI Layer -->
        <mxCell id="ai" value="AI / Agent Layer&#xa;- Classifier&#xa;- Extractor&#xa;- Validator"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;"
          vertex="1" parent="1">
          <mxGeometry x="1100" y="120" width="220" height="300" as="geometry"/>
        </mxCell>

        <!-- Routing -->
        <mxCell id="routing" value="Routing &amp; Decision Layer&#xa;- Business Rules&#xa;- Confidence Check"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;"
          vertex="1" parent="1">
          <mxGeometry x="1340" y="120" width="220" height="300" as="geometry"/>
        </mxCell>

        <!-- Human Loop -->
        <mxCell id="human" value="Human-in-the-loop&#xa;- Review Queue&#xa;- Manual Fix"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;"
          vertex="1" parent="1">
          <mxGeometry x="1340" y="440" width="220" height="160" as="geometry"/>
        </mxCell>

        <!-- Output -->
        <mxCell id="output" value="Integration &amp; Output Layer&#xa;- Claims Backend API&#xa;- SQL Database"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;"
          vertex="1" parent="1">
          <mxGeometry x="1580" y="120" width="220" height="300" as="geometry"/>
        </mxCell>

        <!-- Arrows -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="input" target="ingestion">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="ingestion" target="content">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="content" target="messaging">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="messaging" target="processing">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="processing" target="ai">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="ai" target="routing">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="routing" target="output">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;" edge="1" parent="1" source="routing" target="human">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
