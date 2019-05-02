#
# PySNMP MIB module Juniper-ERX-System-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ERX-System-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniSystemAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniSystemAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, Counter32, ObjectIdentity, TimeTicks, Integer32, NotificationType, Unsigned32, iso, IpAddress, MibIdentifier, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ObjectIdentity", "TimeTicks", "Integer32", "NotificationType", "Unsigned32", "iso", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniErxSystemAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1))
juniErxSystemAgent.setRevisions(('2003-11-24 19:53', '2003-01-28 21:48', '2002-08-19 13:17', '2002-04-01 22:32', '2001-04-13 13:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniErxSystemAgent.setRevisionsDescriptions(('Juniper-System-MIB: Added resource utilization notification enable/disable. Added KByte memory capacilty object.', 'Juniper-System-MIB: Replaced Unisphere names with Juniper names. Added resoure utilization support.', 'Added support for the Juniper generic system MIB.', 'Added thermal protection support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniErxSystemAgent.setLastUpdated('200311241953Z')
if mibBuilder.loadTexts: juniErxSystemAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniErxSystemAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniErxSystemAgent.setDescription('The agent capabilities definitions for the System component of the SNMP agent in the Juniper ERX (E-series) family of products.')
juniErxSystemAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV1 = juniErxSystemAgentV1.setProductRelease('Version 1 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 1.3\n        system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV1 = juniErxSystemAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV1.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when new slot information objects were added.')
juniErxSystemAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV2 = juniErxSystemAgentV2.setProductRelease('Version 2 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV2 = juniErxSystemAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV2.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when the timing group was added.')
juniErxSystemAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV3 = juniErxSystemAgentV3.setProductRelease('Version 3 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 3.0 and\n        3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV3 = juniErxSystemAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV3.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when memory management objects and notifications were added.')
juniErxSystemAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV4 = juniErxSystemAgentV4.setProductRelease('Version 4 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 3.2\n        system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV4 = juniErxSystemAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV4.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when thermal protection support was added.')
juniErxSystemAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV5 = juniErxSystemAgentV5.setProductRelease('Version 5 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component is supported in the JUNOSe 3.3 thru\n        4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV5 = juniErxSystemAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV5.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when the generic system MIB support was added.')
juniErxSystemAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV6 = juniErxSystemAgentV6.setProductRelease('Version 6 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 4.1 and\n        subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV6 = juniErxSystemAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV6.setDescription('The MIBs supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when resource utilization support was added to Juniper-System-MIB.')
juniErxSystemAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV7 = juniErxSystemAgentV7.setProductRelease('Version 7 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component was supported in the JUNOSe 5.0 and\n        5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV7 = juniErxSystemAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniErxSystemAgentV7.setDescription('The MIBs supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe. These capabilities became obsolete when the resource utilization trap enabled and KByte memory capacilty objects were added to Juniper-System-MIB.')
juniErxSystemAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV8 = juniErxSystemAgentV8.setProductRelease('Version 8 of the System component of the JUNOSe SNMP agent.  This\n        version of the ERX System component is supported in the JUNOSe 5.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniErxSystemAgentV8 = juniErxSystemAgentV8.setStatus('current')
if mibBuilder.loadTexts: juniErxSystemAgentV8.setDescription('The MIBs supported by the SNMP agent for the ERX (platform-specific) System application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-ERX-System-CONF", juniErxSystemAgent=juniErxSystemAgent, juniErxSystemAgentV6=juniErxSystemAgentV6, PYSNMP_MODULE_ID=juniErxSystemAgent, juniErxSystemAgentV3=juniErxSystemAgentV3, juniErxSystemAgentV7=juniErxSystemAgentV7, juniErxSystemAgentV8=juniErxSystemAgentV8, juniErxSystemAgentV2=juniErxSystemAgentV2, juniErxSystemAgentV4=juniErxSystemAgentV4, juniErxSystemAgentV1=juniErxSystemAgentV1, juniErxSystemAgentV5=juniErxSystemAgentV5)
