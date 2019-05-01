#
# PySNMP MIB module Juniper-PPPoE-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPPoE-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Unsigned32, Counter64, MibIdentifier, iso, Bits, ObjectIdentity, IpAddress, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Unsigned32", "Counter64", "MibIdentifier", "iso", "Bits", "ObjectIdentity", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPppoeProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4))
juniPppoeProfileAgent.setRevisions(('2005-07-13 11:40', '2004-06-14 20:48', '2003-03-13 18:01', '2002-09-06 16:54', '2002-08-15 20:38', '2002-05-31 18:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPppoeProfileAgent.setRevisionsDescriptions(('Added MTU control object.', 'Added PADR Remote Circuit Id Capture support.', 'Added service name table support.', 'Replaced Unisphere names with Juniper names.', 'Added PADI flag and packet trace support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPppoeProfileAgent.setLastUpdated('200507131140Z')
if mibBuilder.loadTexts: juniPppoeProfileAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPppoeProfileAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPppoeProfileAgent.setDescription('The agent capabilities definitions for the PPPoE Profile component of the SNMP agent in the Juniper E-series family of products.')
juniPppoeProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV1 = juniPppoeProfileAgentV1.setProductRelease('Version 1 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component was supported in JUNOSe 3.0\n        and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV1 = juniPppoeProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in JUNOSe. These capabilities became obsolete when the duplicate MAC address indicator and AC-NAME were added.')
juniPppoeProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV2 = juniPppoeProfileAgentV2.setProductRelease('Version 2 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component was supported in JUNOSe 3.2\n        and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV2 = juniPppoeProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in JUNOSe. These capabilities became obsolete when support was added for PADI flag and packet trace.')
juniPppoeProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV3 = juniPppoeProfileAgentV3.setProductRelease('Version 3 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component was supported in JUNOSe 4.0\n        thru 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV3 = juniPppoeProfileAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in JUNOSe. These capabilities became obsolete when service name table support was added.')
juniPppoeProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV4 = juniPppoeProfileAgentV4.setProductRelease('Version 4 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 5.1 through 7.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV4 = juniPppoeProfileAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileAgentV4.setDescription('The MIB supported by the SNMP agent for the PPPoE application in JUNOSe. These capabilities became obsolete when PADR remote-circuit-id field was added.')
juniPppoeProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV5 = juniPppoeProfileAgentV5.setProductRelease('Version 5 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component is supported in JUNOSe 7.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV5 = juniPppoeProfileAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileAgentV5.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in JUNOSe.')
juniPppoeProfileAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV6 = juniPppoeProfileAgentV6.setProductRelease('Version 6 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component is supported in JUNOSe 7.0.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV6 = juniPppoeProfileAgentV6.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileAgentV6.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-PPPoE-Profile-CONF", PYSNMP_MODULE_ID=juniPppoeProfileAgent, juniPppoeProfileAgentV1=juniPppoeProfileAgentV1, juniPppoeProfileAgent=juniPppoeProfileAgent, juniPppoeProfileAgentV6=juniPppoeProfileAgentV6, juniPppoeProfileAgentV3=juniPppoeProfileAgentV3, juniPppoeProfileAgentV5=juniPppoeProfileAgentV5, juniPppoeProfileAgentV4=juniPppoeProfileAgentV4, juniPppoeProfileAgentV2=juniPppoeProfileAgentV2)
