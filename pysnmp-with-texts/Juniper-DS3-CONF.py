#
# PySNMP MIB module Juniper-DS3-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DS3-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, MibIdentifier, Integer32, ObjectIdentity, IpAddress, NotificationType, Bits, ModuleIdentity, Unsigned32, Gauge32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "MibIdentifier", "Integer32", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "ModuleIdentity", "Unsigned32", "Gauge32", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDs3Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11))
juniDs3Agent.setRevisions(('2003-09-29 21:05', '2003-01-30 19:08', '2003-01-30 16:37', '2002-08-27 18:48', '2001-04-18 19:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDs3Agent.setRevisionsDescriptions(("DS3-MIB: Replaced SMIv1 'groups' (RFC1407-MIB) with SMIv2 conformance groups (DS3-MIB).", 'Juniper-DS3-MIB: Replaced Unisphere names with Juniper names.', 'Juniper-DS3-MIB: Added far end port number, generator number and carrier support.', 'DS3-MIB: Added far end support. Juniper-DS3-MIB: Added far end support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDs3Agent.setLastUpdated('200309292105Z')
if mibBuilder.loadTexts: juniDs3Agent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDs3Agent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDs3Agent.setDescription('The agent capabilities definitions for the DS3 component of the SNMP agent in the Juniper E-series family of products.')
juniDs3AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV1 = juniDs3AgentV1.setProductRelease('Version 1 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV1 = juniDs3AgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs3AgentV1.setDescription('The MIBs supported by the SNMP agent for the DS3 application in JUNOSe. These capabilities became obsolete when support was added for line type and cell scrambler objects.')
juniDs3AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV2 = juniDs3AgentV2.setProductRelease('Version 2 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 1.1 thru JUNOSe 2.5 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV2 = juniDs3AgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs3AgentV2.setDescription('The MIBs supported by the SNMP agent for the DS3 application in JUNOSe. These capabilities became obsolete when support was added for DSU configuration objects.')
juniDs3AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV3 = juniDs3AgentV3.setProductRelease('Version 3 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 2.6 and subsequent JUNOSe\n        2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV3 = juniDs3AgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs3AgentV3.setDescription('The MIBs supported by the SNMP agent for the DS3 application in JUNOSe. These capabilities became obsolete when support was added for dynamic DS3 interface objects.')
juniDs3AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV4 = juniDs3AgentV4.setProductRelease('Version 4 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV4 = juniDs3AgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs3AgentV4.setDescription('The MIBs supported by the SNMP agent for the DS3 application in JUNOSe. These capabilities became obsolete when far end support was added to the Juniper-DS3-MIB.')
juniDs3AgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV5 = juniDs3AgentV5.setProductRelease('Version 5 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV5 = juniDs3AgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs3AgentV5.setDescription('The MIBs supported by the SNMP agent for the DS3 application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-DS3-MIB for far end port number, generator number and carrier.')
juniDs3AgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV6 = juniDs3AgentV6.setProductRelease('Version 6 of the DS3 component of the JUNOSe SNMP agent.  This version\n        of the DS3 component is supported in JUNOSe 4.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs3AgentV6 = juniDs3AgentV6.setStatus('current')
if mibBuilder.loadTexts: juniDs3AgentV6.setDescription('The MIBs supported by the SNMP agent for the DS3 application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-DS3-CONF", juniDs3Agent=juniDs3Agent, juniDs3AgentV5=juniDs3AgentV5, juniDs3AgentV2=juniDs3AgentV2, juniDs3AgentV6=juniDs3AgentV6, PYSNMP_MODULE_ID=juniDs3Agent, juniDs3AgentV1=juniDs3AgentV1, juniDs3AgentV4=juniDs3AgentV4, juniDs3AgentV3=juniDs3AgentV3)
