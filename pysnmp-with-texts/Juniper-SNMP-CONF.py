#
# PySNMP MIB module Juniper-SNMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SNMP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, Integer32, Gauge32, Counter64, iso, IpAddress, ObjectIdentity, NotificationType, MibIdentifier, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Integer32", "Gauge32", "Counter64", "iso", "IpAddress", "ObjectIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSnmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39))
juniSnmpAgent.setRevisions(('2003-03-10 20:27', '2002-09-06 16:54', '2002-08-20 13:29', '2002-08-14 19:23', '2001-10-16 13:44', '2001-04-13 15:44',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSnmpAgent.setRevisionsDescriptions(('Added support for management application type and MIB access permission to the Juniper-SNMP-MIB.', 'Replaced Unisphere names with Juniper names.', 'Added support for ping time window and notification log data inclusion in trap varbinds.', 'Added support for proxy enable/disable feature.', 'Added support for the snmpSetGroup. Added new objects to the Juniper-SNMP-MIB supporting interface compress, trap severities and trap severity filtering.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSnmpAgent.setLastUpdated('200303102027Z')
if mibBuilder.loadTexts: juniSnmpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSnmpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSnmpAgent.setDescription('The agent capabilities definitions for the SNMP entity component of the SNMP agent in the Juniper E-series family of products.')
juniSnmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV1 = juniSnmpAgentV1.setProductRelease('Version 1 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV1 = juniSnmpAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV1.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when SNMPv3 support, View support, and Named Access List support were added.')
juniSnmpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV2 = juniSnmpAgentV2.setProductRelease('Version 2 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 2.0 thru\n        2.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV2 = juniSnmpAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV2.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when the juniSnmpInterfaceMode object was added.')
juniSnmpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV3 = juniSnmpAgentV3.setProductRelease('Version 3 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 2.3 thru\n        3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV3 = juniSnmpAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV3.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when SNMPv2-MIB.sysORTable support was added.')
juniSnmpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV4 = juniSnmpAgentV4.setProductRelease('Version 4 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 3.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV4 = juniSnmpAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV4.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when SNMPv2-MIB.snmpSetGroup support was added and new Juniper SNMP MIB objects were added supporting interface compress, trap severities and trap severity filtering.')
juniSnmpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV5 = juniSnmpAgentV5.setProductRelease('Version 5 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 3.3 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV5 = juniSnmpAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV5.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when support for proxy enable/disable was added.')
juniSnmpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV6 = juniSnmpAgentV6.setProductRelease('Version 6 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component was supported in JUNOSe 3.4 thru\n        4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV6 = juniSnmpAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV6.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-SNMP-MIB for ping time window and notification log data inclusion in trap varbinds.')
juniSnmpAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV7 = juniSnmpAgentV7.setProductRelease('Version 7 of the SNMP entity component of the JUNOSe SNMP\n        agent.  This version of the SNMP entity component is supported in the\n        JUNOSe 4.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV7 = juniSnmpAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV7.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-SNMP-MIB for management application type and MIB access permission.')
juniSnmpAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV8 = juniSnmpAgentV8.setProductRelease('Version 8 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV8 = juniSnmpAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV8.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-SNMP-MIB for trap severity filter based on trap categories.')
juniSnmpAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV9 = juniSnmpAgentV9.setProductRelease('Version 9 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component is supported in JUNOSe 9.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV9 = juniSnmpAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniSnmpAgentV9.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe.')
juniSnmpAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV10 = juniSnmpAgentV10.setProductRelease('Version 10 of the SNMP entity component of the JUNOSe SNMP agent.  This\n        version of the SNMP entity component is supported in JUNOSe 10.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAgentV10 = juniSnmpAgentV10.setStatus('current')
if mibBuilder.loadTexts: juniSnmpAgentV10.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-SNMP-CONF", juniSnmpAgentV8=juniSnmpAgentV8, PYSNMP_MODULE_ID=juniSnmpAgent, juniSnmpAgentV3=juniSnmpAgentV3, juniSnmpAgentV4=juniSnmpAgentV4, juniSnmpAgentV5=juniSnmpAgentV5, juniSnmpAgentV6=juniSnmpAgentV6, juniSnmpAgentV7=juniSnmpAgentV7, juniSnmpAgentV9=juniSnmpAgentV9, juniSnmpAgentV10=juniSnmpAgentV10, juniSnmpAgentV2=juniSnmpAgentV2, juniSnmpAgentV1=juniSnmpAgentV1, juniSnmpAgent=juniSnmpAgent)
