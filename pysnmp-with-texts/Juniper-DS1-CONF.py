#
# PySNMP MIB module Juniper-DS1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DS1-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, IpAddress, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, Unsigned32, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "Unsigned32", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDs1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10))
juniDs1Agent.setRevisions(('2003-09-25 15:23', '2003-01-31 17:15', '2003-01-31 16:37', '2002-05-13 16:34', '2001-03-29 20:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDs1Agent.setRevisionsDescriptions(("DS1-MIB: Replaced SMIv1 'groups' (RFC1406-MIB) with SMIv2 conformance groups (DS1-MIB).", 'Juniper-DS1-MIB: Replaced Unisphere names with Juniper names.', 'Juniper-DS1-MIB: Added support for FDL transmit mode, remote FDL strings and far end FDL carrier.', 'DS1-MIB: Added far end statistics support. Juniper-DS1-MIB: Added far end statistics support. Added FDL support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDs1Agent.setLastUpdated('200309251523Z')
if mibBuilder.loadTexts: juniDs1Agent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDs1Agent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDs1Agent.setDescription('The agent capabilities definitions for the DS1 component of the SNMP agent in the Juniper E-series family of products.')
juniDs1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV1 = juniDs1AgentV1.setProductRelease('Version 1 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV1 = juniDs1AgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs1AgentV1.setDescription('The MIBs supported by the SNMP agent for the DS1 application in JUNOSe. This version became obsolete when new objects were added to the Juniper-DS1-MIB.')
juniDs1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV2 = juniDs1AgentV2.setProductRelease('Version 2 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 1.1 thru JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV2 = juniDs1AgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs1AgentV2.setDescription('The MIBs supported by the SNMP agent for the DS1 application in JUNOSe. This version became obsolete when dynamic DS1 interface support was added to the Juniper-DS1-MIB.')
juniDs1AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV3 = juniDs1AgentV3.setProductRelease('Version 3 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV3 = juniDs1AgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs1AgentV3.setDescription('The MIBs supported by the SNMP agent for the DS1 application in JUNOSe. This version became obsolete when far end statistics support was added and FDL support was added to the Juniper-DS1-MIB.')
juniDs1AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV4 = juniDs1AgentV4.setProductRelease('Version 4 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV4 = juniDs1AgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniDs1AgentV4.setDescription('The MIBs supported by the SNMP agent for the DS1 application in JUNOSe. This version became obsolete when more FDL support was added to the Juniper-DS1-MIB.')
juniDs1AgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV5 = juniDs1AgentV5.setProductRelease('Version 5 of the DS1 component of the JUNOSe SNMP agent.  This version\n        of the DS1 component is supported in JUNOSe 4.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDs1AgentV5 = juniDs1AgentV5.setStatus('current')
if mibBuilder.loadTexts: juniDs1AgentV5.setDescription('The MIBs supported by the SNMP agent for the DS1 application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-DS1-CONF", PYSNMP_MODULE_ID=juniDs1Agent, juniDs1Agent=juniDs1Agent, juniDs1AgentV1=juniDs1AgentV1, juniDs1AgentV4=juniDs1AgentV4, juniDs1AgentV2=juniDs1AgentV2, juniDs1AgentV5=juniDs1AgentV5, juniDs1AgentV3=juniDs1AgentV3)
