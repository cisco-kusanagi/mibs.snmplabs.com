#
# PySNMP MIB module Juniper-PPP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Counter64, IpAddress, NotificationType, TimeTicks, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, ObjectIdentity, ModuleIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "IpAddress", "NotificationType", "TimeTicks", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPppAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32))
juniPppAgent.setRevisions(('2010-02-09 11:06', '2009-09-18 07:24', '2009-08-10 14:23', '2008-08-27 13:18', '2007-07-12 12:15', '2005-10-19 16:26', '2004-10-01 21:41', '2003-11-03 18:32', '2003-09-24 20:11', '2003-01-28 15:47', '2002-08-30 20:36', '2002-05-09 21:03', '2002-05-08 20:25', '2001-04-10 18:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPppAgent.setRevisionsDescriptions(('Added new juniPppGeneralAgentV9.', 'Added new multiclass multilink objects. Added new traffic class mapping for multiclasses.juniPppMultiLinkAgentV10 was added.', 'Added juniPppGeneralAgentV8', 'Added juniPppGeneralAgentV7', 'Updated juniPppLcpGroup and juniPppMlPppGroup to add ignore magic number. Updated juniPppLcpGroup and juniPppMlpppGroup.', 'Juniper-PPP-MIB: Added new object to the multi-link group.', 'Updated the juniPppSummary table', 'Juniper-PPP-MIB: Added new objects to the multi-link group.', 'Juniper-PPP-MIB: Added IPv6 support.', 'Juniper-PPP-MIB: Replaced Unisphere names with Juniper names. Added new objects to the multi-link group.', 'Juniper-PPP-MIB: Added new objects to the LCP and multi-link groups.', 'Juniper-PPP-MIB: Added new objects to the LCP, IP and multi-link groups.', 'Created separate capabilities for multi-link PPP.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPppAgent.setLastUpdated('201002091106Z')
if mibBuilder.loadTexts: juniPppAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPppAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPppAgent.setDescription('The agent capabilities definitions for the point-to-point protocol (PPP) component of the SNMP agent in the Juniper E-series family of products.')
juniPppAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppAgentV1 = juniPppAgentV1.setProductRelease('Version 1 of the PPP component of the JUNOSe SNMP agent.  This version\n        of the PPP component was supported in JUNOSe 2.4 thru 3.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppAgentV1 = juniPppAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppAgentV1.setDescription('The MIBs supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when the multilink capabilities were separated out.')
juniPppGeneralAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2))
if mibBuilder.loadTexts: juniPppGeneralAgent.setStatus('current')
if mibBuilder.loadTexts: juniPppGeneralAgent.setDescription('The registration group of agent capabilities for the general functionality of the PPP application which provides management support for basic (non-multi-link) PPP interfaces via SNMP.')
juniPppGeneralAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV1 = juniPppGeneralAgentV1.setProductRelease('Version 1 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 3.3 and subsequent\n        3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV1 = juniPppGeneralAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV1.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when new LCP and IP objects were added to the Juniper-PPP-MIB.')
juniPppGeneralAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV2 = juniPppGeneralAgentV2.setProductRelease('Version 2 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV2 = juniPppGeneralAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV2.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when new LCP objects were added to the Juniper-PPP-MIB.')
juniPppGeneralAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV3 = juniPppGeneralAgentV3.setProductRelease('Version 3 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 4.1 through 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV3 = juniPppGeneralAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV3.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when IPv6 support was added.')
juniPppGeneralAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV4 = juniPppGeneralAgentV4.setProductRelease('Version 4 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component was supported in JUNOSe 5.1 and subsequent\n        5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV4 = juniPppGeneralAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV4.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when new objects were added.')
juniPppGeneralAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV5 = juniPppGeneralAgentV5.setProductRelease('Version 5 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 6.0 throught 7.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV5 = juniPppGeneralAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV5.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when new objects were added.')
juniPppGeneralAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV6 = juniPppGeneralAgentV6.setProductRelease('Version 6 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 7.3 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV6 = juniPppGeneralAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV6.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when new objects were added.')
juniPppGeneralAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV7 = juniPppGeneralAgentV7.setProductRelease('Version 7 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 10.1 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV7 = juniPppGeneralAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV7.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe.')
juniPppGeneralAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV8 = juniPppGeneralAgentV8.setProductRelease('Version 8 of the general PPP component of the JUNOSe SNMP agent.  This\n        version of the PPP component is supported in JUNOSe 11.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV8 = juniPppGeneralAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppGeneralAgentV8.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe.These capabilities became obsolete when new objects were added.')
juniPppGeneralAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV9 = juniPppGeneralAgentV9.setProductRelease('Version 9 of the general PPP component of the JUNOSe SNMP agent. This\n        version of the PPP component is supported in JUNOSe 11.2 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppGeneralAgentV9 = juniPppGeneralAgentV9.setStatus('current')
if mibBuilder.loadTexts: juniPppGeneralAgentV9.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe.')
juniPppMultiLinkAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3))
if mibBuilder.loadTexts: juniPppMultiLinkAgent.setStatus('current')
if mibBuilder.loadTexts: juniPppMultiLinkAgent.setDescription('The registration group of agent capabilities for the multi-link functionality of the PPP application which provides management support for multi-link PPP interfaces via SNMP.')
juniPppMultiLinkAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV1 = juniPppMultiLinkAgentV1.setProductRelease('Version 1 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 3.3 and\n        subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV1 = juniPppMultiLinkAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV1.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB.')
juniPppMultiLinkAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV2 = juniPppMultiLinkAgentV2.setProductRelease('Version 2 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV2 = juniPppMultiLinkAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV2.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB')
juniPppMultiLinkAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV3 = juniPppMultiLinkAgentV3.setProductRelease('Version 3 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 4.1 and\n        subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV3 = juniPppMultiLinkAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV3.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB')
juniPppMultiLinkAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV4 = juniPppMultiLinkAgentV4.setProductRelease('Version 4 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 5.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV4 = juniPppMultiLinkAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV4.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when IPv6 support was added.')
juniPppMultiLinkAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV5 = juniPppMultiLinkAgentV5.setProductRelease('Version 5 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 5.1 and 5.2\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV5 = juniPppMultiLinkAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV5.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB.')
juniPppMultiLinkAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV6 = juniPppMultiLinkAgentV6.setProductRelease('Version 6 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 5.1 and \n        subsequent 5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV6 = juniPppMultiLinkAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV6.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB.')
juniPppMultiLinkAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV7 = juniPppMultiLinkAgentV7.setProductRelease('Version 7 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component is supported in JUNOSe 6.0 through\n        7.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV7 = juniPppMultiLinkAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV7.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB.')
juniPppMultiLinkAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV8 = juniPppMultiLinkAgentV8.setProductRelease('Version 8 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component is supported in JUNOSe 7.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV8 = juniPppMultiLinkAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV8.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB.')
juniPppMultiLinkAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV9 = juniPppMultiLinkAgentV9.setProductRelease('Version 9 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 7.3 and \n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV9 = juniPppMultiLinkAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV9.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe. These capabilities became obsolete when new multi-link objects were added to the Juniper-PPP-MIB.')
juniPppMultiLinkAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV10 = juniPppMultiLinkAgentV10.setProductRelease('Version 10 of the multi-link PPP component of the JUNOSe SNMP agent.\n        This version of the PPP component was supported in JUNOSe 11.1 and \n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppMultiLinkAgentV10 = juniPppMultiLinkAgentV10.setStatus('current')
if mibBuilder.loadTexts: juniPppMultiLinkAgentV10.setDescription('The MIB groups supported by the SNMP agent for the PPP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-PPP-CONF", juniPppGeneralAgentV6=juniPppGeneralAgentV6, juniPppMultiLinkAgentV2=juniPppMultiLinkAgentV2, juniPppGeneralAgentV7=juniPppGeneralAgentV7, juniPppGeneralAgentV2=juniPppGeneralAgentV2, juniPppMultiLinkAgentV9=juniPppMultiLinkAgentV9, juniPppMultiLinkAgentV5=juniPppMultiLinkAgentV5, juniPppGeneralAgentV4=juniPppGeneralAgentV4, juniPppMultiLinkAgentV8=juniPppMultiLinkAgentV8, juniPppMultiLinkAgentV10=juniPppMultiLinkAgentV10, juniPppMultiLinkAgentV3=juniPppMultiLinkAgentV3, juniPppMultiLinkAgentV7=juniPppMultiLinkAgentV7, juniPppMultiLinkAgent=juniPppMultiLinkAgent, juniPppGeneralAgentV5=juniPppGeneralAgentV5, juniPppGeneralAgent=juniPppGeneralAgent, juniPppMultiLinkAgentV1=juniPppMultiLinkAgentV1, juniPppGeneralAgentV8=juniPppGeneralAgentV8, juniPppAgent=juniPppAgent, juniPppGeneralAgentV3=juniPppGeneralAgentV3, PYSNMP_MODULE_ID=juniPppAgent, juniPppGeneralAgentV1=juniPppGeneralAgentV1, juniPppMultiLinkAgentV4=juniPppMultiLinkAgentV4, juniPppMultiLinkAgentV6=juniPppMultiLinkAgentV6, juniPppGeneralAgentV9=juniPppGeneralAgentV9, juniPppAgentV1=juniPppAgentV1)
