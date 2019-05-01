#
# PySNMP MIB module Juniper-PPP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPP-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, iso, TimeTicks, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, IpAddress, ObjectIdentity, Gauge32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "iso", "TimeTicks", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Gauge32", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPppProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3))
juniPppProfileAgent.setRevisions(('2009-09-18 07:24', '2009-08-10 14:23', '2007-07-12 12:15', '2005-10-19 16:26', '2003-11-03 21:32', '2003-03-13 16:47', '2002-09-06 16:54', '2002-09-03 22:38', '2002-01-25 14:10', '2002-01-16 17:58', '2002-01-08 19:43', '2001-10-17 17:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPppProfileAgent.setRevisionsDescriptions(('Added new multiclass multilink objects. Added new traffic class mapping for multiclasses.juniPppProfileAgentV11 was added.', 'Added new IPCP prompt option DNS object', 'Added new ignore magic number mismatch object Added juniPppProfileLcpAuthentication2 object.', 'Juniper-PPP-PROFILE-MIB: Added hash-based link selection option for MLPPP.', 'Juniper-PPP-PROFILE-MIB: Added MLPPP fragmentation and reassembly parameters.', 'Added juniPppProfileInitiateIp and juniPppProfileInitiateIpv6 objects.', 'Replaced Unisphere names with Juniper names.', 'Added the AAA profile ID object.', 'Added the authenticator virtual router object.', 'Added the IPCP netmask option object.', 'Added support for dynamic multi-link PPP (MLPPP) interfaces.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPppProfileAgent.setLastUpdated('200909180724Z')
if mibBuilder.loadTexts: juniPppProfileAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPppProfileAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPppProfileAgent.setDescription('The agent capabilities definitions for the PPP Profile component of the SNMP agent in the Juniper E-series family of products.')
juniPppProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV1 = juniPppProfileAgentV1.setProductRelease('Version 1 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 3.0 through\n        3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV1 = juniPppProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the dynamic multilink PPP object was added.')
juniPppProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV2 = juniPppProfileAgentV2.setProductRelease('Version 2 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 3.3 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV2 = juniPppProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the IPCP netmask option object was added.')
juniPppProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV3 = juniPppProfileAgentV3.setProductRelease('Version 3 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 3.4 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV3 = juniPppProfileAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the authenticator virtual router object was added.')
juniPppProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV4 = juniPppProfileAgentV4.setProductRelease('Version 4 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV4 = juniPppProfileAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV4.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the AAA profile ID object was added.')
juniPppProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV5 = juniPppProfileAgentV5.setProductRelease('Version 5 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 4.1 through\n        5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV5 = juniPppProfileAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV5.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the Initiate IP and Initiate IPv6 objects were added.')
juniPppProfileAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV6 = juniPppProfileAgentV6.setProductRelease('Version 6 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component was supported in JUNOSe 5.1 and 5.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV6 = juniPppProfileAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV6.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the MLPPP fragmentation and reassembly parameters were added.')
juniPppProfileAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV7 = juniPppProfileAgentV7.setProductRelease('Version 7 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 5.3 through\n        7.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV7 = juniPppProfileAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV7.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when the hash-based link selction option was added to MLPPP.')
juniPppProfileAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV8 = juniPppProfileAgentV8.setProductRelease('Version 8 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 7.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV8 = juniPppProfileAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV8.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when object rsPppProfileLcpAuthentication2 was added.')
juniPppProfileAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV9 = juniPppProfileAgentV9.setProductRelease('Version 9 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 7.3 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV9 = juniPppProfileAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV9.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe. These capabilities became obsolete when object rsPppProfileIpcpDnsOption and rsPppProfileIpcpLockout was added')
juniPppProfileAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV10 = juniPppProfileAgentV10.setProductRelease('Version 10 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 11.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV10 = juniPppProfileAgentV10.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppProfileAgentV10.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe.These capabilities became obsolete when support for Multiclass MLPPP was added.')
juniPppProfileAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV11 = juniPppProfileAgentV11.setProductRelease('Version 11 of the PPP Profile component of the JUNOSe SNMP agent.  This\n        version of the PPP Profile component is supported in JUNOSe 11.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileAgentV11 = juniPppProfileAgentV11.setStatus('current')
if mibBuilder.loadTexts: juniPppProfileAgentV11.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-PPP-Profile-CONF", juniPppProfileAgentV5=juniPppProfileAgentV5, juniPppProfileAgentV1=juniPppProfileAgentV1, juniPppProfileAgentV9=juniPppProfileAgentV9, juniPppProfileAgentV8=juniPppProfileAgentV8, juniPppProfileAgentV6=juniPppProfileAgentV6, juniPppProfileAgentV10=juniPppProfileAgentV10, juniPppProfileAgent=juniPppProfileAgent, juniPppProfileAgentV11=juniPppProfileAgentV11, juniPppProfileAgentV2=juniPppProfileAgentV2, juniPppProfileAgentV7=juniPppProfileAgentV7, PYSNMP_MODULE_ID=juniPppProfileAgent, juniPppProfileAgentV3=juniPppProfileAgentV3, juniPppProfileAgentV4=juniPppProfileAgentV4)
