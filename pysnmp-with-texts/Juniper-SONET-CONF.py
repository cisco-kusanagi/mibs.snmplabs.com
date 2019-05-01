#
# PySNMP MIB module Juniper-SONET-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SONET-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, Counter64, IpAddress, Bits, Unsigned32, Gauge32, TimeTicks, NotificationType, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "Counter64", "IpAddress", "Bits", "Unsigned32", "Gauge32", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSonetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40))
juniSonetAgent.setRevisions(('2005-09-15 20:26', '2003-07-16 17:22', '2003-01-31 20:09', '2002-04-09 23:44', '2002-02-04 21:35', '2001-04-03 22:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSonetAgent.setRevisionsDescriptions(('APS-MIB - mib added.', 'Juniper-UNI-SONET-MIB: Added path event status and notification support.', 'Juniper-UNI-SONET-MIB: Replaced Unisphere names with Juniper names.', 'APS-MIB-JUNI: Added support for IETF draft-ietf-atommib-sonetaps-mib-05 as a Juniper experimental MIB.', 'Separate out the SONET VT support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSonetAgent.setLastUpdated('200509152026Z')
if mibBuilder.loadTexts: juniSonetAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSonetAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSonetAgent.setDescription('The agent capabilities definitions for the SONET component of the SNMP agent in the Juniper E-series family of products.')
juniSonetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV1 = juniSonetAgentV1.setProductRelease('Version 1 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV1 = juniSonetAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetAgentV1.setDescription('The MIBs supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when support for the standard VT group was added.')
juniSonetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV2 = juniSonetAgentV2.setProductRelease('Version 2 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV2 = juniSonetAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetAgentV2.setDescription('The MIBs supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when support for the proprietary path and VT groups were added.')
juniSonetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV3 = juniSonetAgentV3.setProductRelease('Version 3 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 3.0 and 3.1\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV3 = juniSonetAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetAgentV3.setDescription('The MIBs supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when support for the RFC-2558 version of the SONET-MIB and far-end statistics were added.')
juniSonetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV4 = juniSonetAgentV4.setProductRelease('Version 4 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 3.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV4 = juniSonetAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetAgentV4.setDescription('The MIBs supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when Virtual Tributary (VT) support was searated out into a separate capabilities statement.')
juniSonetBasicAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5))
juniSonetBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV1 = juniSonetBasicAgentV1.setProductRelease('Version 1 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component was supported in JUNOSe 3.3 and subsequent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV1 = juniSonetBasicAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetBasicAgentV1.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when support was added for the Internet draft of the APS MIB.')
juniSonetBasicAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV2 = juniSonetBasicAgentV2.setProductRelease('Version 2 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component was supported in JUNOSe 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV2 = juniSonetBasicAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetBasicAgentV2.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when new medium and path controls were added.')
juniSonetBasicAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV3 = juniSonetBasicAgentV3.setProductRelease('Version 3 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV3 = juniSonetBasicAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetBasicAgentV3.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in JUNOSe. These capabilities became obsolete when path event status and notification support was added.')
juniSonetBasicAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV4 = juniSonetBasicAgentV4.setProductRelease('Version 4 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component is supported in JUNOSe 5.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV4 = juniSonetBasicAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniSonetBasicAgentV4.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in JUNOSe.')
juniSonetBasicAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV5 = juniSonetBasicAgentV5.setProductRelease('Version 5 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component is supported in JUNOSe 7.2 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV5 = juniSonetBasicAgentV5.setStatus('current')
if mibBuilder.loadTexts: juniSonetBasicAgentV5.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in JUNOSe.')
juniSonetVTAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6))
juniSonetVTAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetVTAgentV1 = juniSonetVTAgentV1.setProductRelease('Version 1 of the SONET VT component of the JUNOSe SNMP agent.  This\n        version of the SONET component is supported in JUNOSe 3.3 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetVTAgentV1 = juniSonetVTAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniSonetVTAgentV1.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-SONET-CONF", juniSonetAgent=juniSonetAgent, juniSonetBasicAgentV3=juniSonetBasicAgentV3, juniSonetAgentV4=juniSonetAgentV4, PYSNMP_MODULE_ID=juniSonetAgent, juniSonetBasicAgentV5=juniSonetBasicAgentV5, juniSonetAgentV1=juniSonetAgentV1, juniSonetBasicAgentV1=juniSonetBasicAgentV1, juniSonetAgentV3=juniSonetAgentV3, juniSonetBasicAgentV4=juniSonetBasicAgentV4, juniSonetAgentV2=juniSonetAgentV2, juniSonetVTAgentV1=juniSonetVTAgentV1, juniSonetBasicAgent=juniSonetBasicAgent, juniSonetBasicAgentV2=juniSonetBasicAgentV2, juniSonetVTAgent=juniSonetVTAgent)
