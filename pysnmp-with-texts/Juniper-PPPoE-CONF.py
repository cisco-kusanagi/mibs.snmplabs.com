#
# PySNMP MIB module Juniper-PPPoE-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPPoE-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, Unsigned32, MibIdentifier, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Bits, Counter64, Counter32, IpAddress, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Bits", "Counter64", "Counter32", "IpAddress", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPppoeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33))
juniPppoeAgent.setRevisions(('2008-11-27 10:23', '2005-08-03 20:58', '2005-07-13 11:40', '2004-06-14 20:48', '2003-03-10 18:48', '2002-12-23 19:41', '2002-10-01 18:37', '2002-08-19 15:14', '2001-06-19 14:27', '2001-04-02 19:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPppoeAgent.setRevisionsDescriptions(('Added unknownAction configuration support in PPPoE service name table', 'Added Interface Lockout configuration and state support.', 'Added MTU control object.', 'Added PADR Remote Circuit Id Capture support.', 'Replaced invalid session counter with separate PADI and PADR invalid session counters. Added invalid length and invalid tag length counters. Added ServiceName table support.', 'Replaced Unisphere names with Juniper names.', 'Added PADN counter.', 'Added PADI flag support.', 'Added AC-NAME and duplicate MAC address indicator objects.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPppoeAgent.setLastUpdated('200811271023Z')
if mibBuilder.loadTexts: juniPppoeAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPppoeAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPppoeAgent.setDescription('The agent capabilities definitions for the point-to-point protocol over Ethernet (PPPoE) component of the SNMP agent in JUNOSe family of products.')
juniPppoeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV1 = juniPppoeAgentV1.setProductRelease('Version 1 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 3.0 thru 3.2.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV1 = juniPppoeAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV1.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when AC-NAME and duplicate MAC address indicator objects were added.')
juniPppoeAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV2 = juniPppoeAgentV2.setProductRelease('Version 2 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 3.2.3 through 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV2 = juniPppoeAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV2.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when PADI flag support was added.')
juniPppoeAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV3 = juniPppoeAgentV3.setProductRelease('Version 3 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV3 = juniPppoeAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV3.setDescription('The MIB supported by the SNMP agent for the PPPoE application in the JUNOSe. These capabilities became obsolete when PADN counter support was added.')
juniPppoeAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV4 = juniPppoeAgentV4.setProductRelease('Version 4 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 4.1 through 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV4 = juniPppoeAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV4.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when the invalid session counter was replaced by separate PADI and PADR invalid session counters, invalid length and invalid tag length counters and service name table support were added.')
juniPppoeAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV5 = juniPppoeAgentV5.setProductRelease('Version 5 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 5.1 through 7.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV5 = juniPppoeAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV5.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when PADR remote-circuit-id field was added.')
juniPppoeAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV6 = juniPppoeAgentV6.setProductRelease('Version 6 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 7.0 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV6 = juniPppoeAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV6.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when MTU configuration was added.')
juniPppoeAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV7 = juniPppoeAgentV7.setProductRelease('Version 7 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 7.0.1 through 7.1\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV7 = juniPppoeAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV7.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when lockout configuration was added.')
juniPppoeAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV8 = juniPppoeAgentV8.setProductRelease('Version 8 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 7.2 through 9.3 \n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV8 = juniPppoeAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeAgentV8.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when unknownAction option was added to PPPoE service name table.')
juniPppoeAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV9 = juniPppoeAgentV9.setProductRelease('Version 9 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component is supported in JUNOSe 10.1 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeAgentV9 = juniPppoeAgentV9.setStatus('current')
if mibBuilder.loadTexts: juniPppoeAgentV9.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-PPPoE-CONF", juniPppoeAgentV5=juniPppoeAgentV5, juniPppoeAgentV4=juniPppoeAgentV4, juniPppoeAgentV3=juniPppoeAgentV3, juniPppoeAgentV8=juniPppoeAgentV8, juniPppoeAgentV7=juniPppoeAgentV7, juniPppoeAgentV9=juniPppoeAgentV9, juniPppoeAgent=juniPppoeAgent, juniPppoeAgentV2=juniPppoeAgentV2, juniPppoeAgentV6=juniPppoeAgentV6, PYSNMP_MODULE_ID=juniPppoeAgent, juniPppoeAgentV1=juniPppoeAgentV1)
