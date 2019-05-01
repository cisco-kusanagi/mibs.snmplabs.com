#
# PySNMP MIB module Juniper-IP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, ObjectIdentity, iso, Counter64, Gauge32, IpAddress, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "iso", "Counter64", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIpProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2))
juniIpProfileAgent.setRevisions(('2006-09-08 10:26', '2005-09-13 17:21', '2004-10-05 14:04', '2003-09-24 15:33', '2002-10-09 14:31', '2001-03-28 21:43',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIpProfileAgent.setRevisionsDescriptions(('Added support for Blocking multicast sources on IP Interfaces - rsIpProfileBlockMulticastSources.', 'Added support for Flow Stats a.k.a. J-Flow for IP Interfaces - rsIpProfileFlowStats.', 'Added support for IP filter options all for IP Interfaces - rsIpProfileFilterOptionsAll.', 'Added support for TCP MSS configuration of IP Interfaces - rsIpProfileTcpMss.', 'Replaced Unisphere names with Juniper names. Obsoleted loopback objects for unnumbered interfaces and added inherited numbered interface objects in juniIpProfileTable (required the addition of juniIpProfileGroup3).', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIpProfileAgent.setLastUpdated('200609081026Z')
if mibBuilder.loadTexts: juniIpProfileAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIpProfileAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIpProfileAgent.setDescription('The agent capabilities definitions for the IP Profile Manager component of the SNMP agent in the Juniper E-series family of products.')
juniIpProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV1 = juniIpProfileAgentV1.setProductRelease('Version 1 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 1.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV1 = juniIpProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe. These capabilities became obsolete when the profile loopback object changed.')
juniIpProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV2 = juniIpProfileAgentV2.setProductRelease('Version 2 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV2 = juniIpProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe. These capabilities became obsolete when juniIpProfileRowStatus was deprecate and the juniIpProfileSetMap and juniIpProfileSrcAddrValidEnable objects were added.')
juniIpProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV3 = juniIpProfileAgentV3.setProductRelease('Version 3 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 3.0\n        through 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV3 = juniIpProfileAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe. These capabilities became obsolete when juniIpProfileLoopback was made obsolete and the juniIpProfileInheritNumString object was added.')
juniIpProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV4 = juniIpProfileAgentV4.setProductRelease('Version 4 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 5.0\n        and 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV4 = juniIpProfileAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV4.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe. These capabilities were made obsolete when TCP MSS configuration support for IP Interface was added.')
juniIpProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV5 = juniIpProfileAgentV5.setProductRelease('Version 5 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component was supported in JUNOSe 5.2, 5.3, and 6.x\n        Now obsolete after IP filter options all support')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV5 = juniIpProfileAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV5.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe.')
juniIpProfileAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV6 = juniIpProfileAgentV6.setProductRelease('Version 6 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component is supported in JUNOSe 7.0\n        and subsequent system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV6 = juniIpProfileAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV6.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe.')
juniIpProfileAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV7 = juniIpProfileAgentV7.setProductRelease('Version 7 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component is supported in JUNOSe 7.2\n        and subsequent system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV7 = juniIpProfileAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpProfileAgentV7.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe.')
juniIpProfileAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV8 = juniIpProfileAgentV8.setProductRelease('Version 8 of the IP Profile component of the JUNOSe SNMP agent.  This\n        version of the IP Profile Manager component is supported in JUNOSe 8.1\n        and subsequent system releases. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileAgentV8 = juniIpProfileAgentV8.setStatus('current')
if mibBuilder.loadTexts: juniIpProfileAgentV8.setDescription('The MIB supported by the SNMP agent for the IP Profile Manager application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-IP-Profile-CONF", juniIpProfileAgentV3=juniIpProfileAgentV3, juniIpProfileAgentV2=juniIpProfileAgentV2, juniIpProfileAgentV4=juniIpProfileAgentV4, PYSNMP_MODULE_ID=juniIpProfileAgent, juniIpProfileAgentV6=juniIpProfileAgentV6, juniIpProfileAgentV5=juniIpProfileAgentV5, juniIpProfileAgentV7=juniIpProfileAgentV7, juniIpProfileAgentV8=juniIpProfileAgentV8, juniIpProfileAgent=juniIpProfileAgent, juniIpProfileAgentV1=juniIpProfileAgentV1)
