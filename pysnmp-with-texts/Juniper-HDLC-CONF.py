#
# PySNMP MIB module Juniper-HDLC-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-HDLC-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, IpAddress, Integer32, Bits, TimeTicks, Counter32, ObjectIdentity, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "Integer32", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniHdlcAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18))
juniHdlcAgent.setRevisions(('2003-09-29 15:19', '2002-09-06 16:54', '2001-03-28 14:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniHdlcAgent.setRevisionsDescriptions(('Added support for HDLC interface idle character.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniHdlcAgent.setLastUpdated('200309291519Z')
if mibBuilder.loadTexts: juniHdlcAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniHdlcAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniHdlcAgent.setDescription('The agent capabilities definitions for the HDLC component of the SNMP agent in the Juniper E-series family of products.')
juniHdlcAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV1 = juniHdlcAgentV1.setProductRelease('Version 1 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component was supported in JUNOSe 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV1 = juniHdlcAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniHdlcAgentV1.setDescription('The MIB supported by the SNMP agent for the HDLC application in JUNOSe. These capabilities became obsolete when juniHdlcIfDataPolarity was added.')
juniHdlcAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV2 = juniHdlcAgentV2.setProductRelease('Version 2 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component was supported in JUNOSe 1.1 thru 3.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV2 = juniHdlcAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniHdlcAgentV2.setDescription('The MIB supported by the SNMP agent for the HDLC application in JUNOSe. These capabilities became obsolete when more objects were added.')
juniHdlcAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV3 = juniHdlcAgentV3.setProductRelease('Version 3 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component is supported in JUNOSe 3.1 through 5.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV3 = juniHdlcAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniHdlcAgentV3.setDescription('The MIB supported by the SNMP agent for the HDLC application in JUNOSe. These capabilities became obsolete when HDLC interface idle character support was added.')
juniHdlcAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV4 = juniHdlcAgentV4.setProductRelease('Version 3 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component is supported in JUNOSe 5.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV4 = juniHdlcAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniHdlcAgentV4.setDescription('The MIB supported by the SNMP agent for the HDLC application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-HDLC-CONF", juniHdlcAgentV2=juniHdlcAgentV2, PYSNMP_MODULE_ID=juniHdlcAgent, juniHdlcAgentV3=juniHdlcAgentV3, juniHdlcAgent=juniHdlcAgent, juniHdlcAgentV1=juniHdlcAgentV1, juniHdlcAgentV4=juniHdlcAgentV4)
