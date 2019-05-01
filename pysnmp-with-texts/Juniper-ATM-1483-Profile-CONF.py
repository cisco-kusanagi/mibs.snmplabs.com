#
# PySNMP MIB module Juniper-ATM-1483-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ATM-1483-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Counter32, Counter64, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniAtm1483ProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6))
juniAtm1483ProfileAgent.setRevisions(('2004-07-26 19:54', '2004-11-02 21:07', '2004-11-02 21:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniAtm1483ProfileAgent.setRevisionsDescriptions(('Added Encapsulation Type Lockout objects.', 'Added ifALias support to profile entries.', 'The initial release of this management information module. Added support for OAM admin status and loopback frequency.',))
if mibBuilder.loadTexts: juniAtm1483ProfileAgent.setLastUpdated('200407261954Z')
if mibBuilder.loadTexts: juniAtm1483ProfileAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniAtm1483ProfileAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniAtm1483ProfileAgent.setDescription('The agent capabilities definitions for the ATM 1483 Profile component of the SNMP agent in the Juniper E-series family of products.')
juniAtm1483ProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV1 = juniAtm1483ProfileAgentV1.setProductRelease('Version 1 of the ATM 1483 Profile component of the JUNOSe SNMP agent.\n        This version of the ATM 1483 Profile component was supported in Juniper\n        JUNOSe 5.1 and 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV1 = juniAtm1483ProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtm1483ProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the ATM 1483 Profile application in JUNOSe. These capabilities became obsolete when ifALias support was added to profile entries.')
juniAtm1483ProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV2 = juniAtm1483ProfileAgentV2.setProductRelease('Version 2 of the ATM 1483 Profile component of the JUNOSe SNMP agent.\n        This version of the ATM 1483 Profile component was supported in Juniper\n        JUNOSe 5.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV2 = juniAtm1483ProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtm1483ProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the ATM 1483 Profile application in JUNOSe. These capabilities became obsolete when OAM support was added to profile entries.')
juniAtm1483ProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV3 = juniAtm1483ProfileAgentV3.setProductRelease('Version 3 of the ATM 1483 Profile component of the JUNOSe SNMP agent.\n        This version of the ATM 1483 Profile component was supported in Juniper\n        JUNOSe 5.1 and 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV3 = juniAtm1483ProfileAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtm1483ProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the ATM 1483 Profile application in JUNOSe. These capabilities became obsolete when ifALias support was added to profile entries.')
juniAtm1483ProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV4 = juniAtm1483ProfileAgentV4.setProductRelease('Version 4 of the ATM 1483 Profile component of the JUNOSe SNMP agent.\n        This version of the ATM 1483 Profile component was supported in Juniper\n        JUNOSe 5.3, 6.0, and 6.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV4 = juniAtm1483ProfileAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniAtm1483ProfileAgentV4.setDescription('')
juniAtm1483ProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV5 = juniAtm1483ProfileAgentV5.setProductRelease('Version 5 of the ATM 1483 Profile component of the JUNOSe SNMP agent.\n        This version of the ATM 1483 Profile component is supported in Juniper\n        JUNOSe 7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileAgentV5 = juniAtm1483ProfileAgentV5.setStatus('current')
if mibBuilder.loadTexts: juniAtm1483ProfileAgentV5.setDescription('')
mibBuilder.exportSymbols("Juniper-ATM-1483-Profile-CONF", juniAtm1483ProfileAgentV4=juniAtm1483ProfileAgentV4, juniAtm1483ProfileAgentV1=juniAtm1483ProfileAgentV1, juniAtm1483ProfileAgentV2=juniAtm1483ProfileAgentV2, juniAtm1483ProfileAgent=juniAtm1483ProfileAgent, juniAtm1483ProfileAgentV5=juniAtm1483ProfileAgentV5, juniAtm1483ProfileAgentV3=juniAtm1483ProfileAgentV3, PYSNMP_MODULE_ID=juniAtm1483ProfileAgent)
