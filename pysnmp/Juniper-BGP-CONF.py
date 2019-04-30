#
# PySNMP MIB module Juniper-BGP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-BGP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, Counter32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ModuleIdentity, NotificationType, TimeTicks, ObjectIdentity, Bits, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ModuleIdentity", "NotificationType", "TimeTicks", "ObjectIdentity", "Bits", "Integer32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniBgpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4))
juniBgpAgent.setRevisions(('2007-05-11 05:17', '2003-12-18 15:28', '2003-12-18 14:27', '2003-07-09 21:35', '2002-11-06 16:33', '2002-09-05 12:56', '2002-09-04 17:56', '2002-03-01 17:51', '2002-01-23 13:16', '2001-12-04 16:09', '2001-12-03 18:48',))
if mibBuilder.loadTexts: juniBgpAgent.setLastUpdated('200705110517Z')
if mibBuilder.loadTexts: juniBgpAgent.setOrganization('Juniper Networks, Inc.')
juniBgpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV1 = juniBgpAgentV1.setProductRelease('Version 1 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.0 and 3.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV1 = juniBgpAgentV1.setStatus('obsolete')
juniBgpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV2 = juniBgpAgentV2.setProductRelease('Version 2 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV2 = juniBgpAgentV2.setStatus('obsolete')
juniBgpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV3 = juniBgpAgentV3.setProductRelease('Version 3 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV3 = juniBgpAgentV3.setStatus('obsolete')
juniBgpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV4 = juniBgpAgentV4.setProductRelease('Version 4 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.4 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV4 = juniBgpAgentV4.setStatus('obsolete')
juniBgpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV5 = juniBgpAgentV5.setProductRelease('Version 5 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 3.5 and subseguent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV5 = juniBgpAgentV5.setStatus('obsolete')
juniBgpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV6 = juniBgpAgentV6.setProductRelease('Version 6 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV6 = juniBgpAgentV6.setStatus('obsolete')
juniBgpAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV7 = juniBgpAgentV7.setProductRelease('Version 7 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 4.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV7 = juniBgpAgentV7.setStatus('obsolete')
juniBgpAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV8 = juniBgpAgentV8.setProductRelease('Version 8 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV8 = juniBgpAgentV8.setStatus('obsolete')
juniBgpAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV9 = juniBgpAgentV9.setProductRelease('Version 9 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV9 = juniBgpAgentV9.setStatus('obsolete')
juniBgpAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV10 = juniBgpAgentV10.setProductRelease('Version 10 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component was supported in JUNOSe 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV10 = juniBgpAgentV10.setStatus('obsolete')
juniBgpAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV11 = juniBgpAgentV11.setProductRelease('Version 11 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component is supported in JUNOSe 5.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV11 = juniBgpAgentV11.setStatus('obsolete')
juniBgpAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV12 = juniBgpAgentV12.setProductRelease('Version 12 of the BGP component of the JUNOSe SNMP agent.  This version\n        of the BGP component is supported in JUNOSe 9.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBgpAgentV12 = juniBgpAgentV12.setStatus('current')
mibBuilder.exportSymbols("Juniper-BGP-CONF", juniBgpAgentV6=juniBgpAgentV6, juniBgpAgentV12=juniBgpAgentV12, juniBgpAgentV10=juniBgpAgentV10, juniBgpAgentV7=juniBgpAgentV7, juniBgpAgentV5=juniBgpAgentV5, juniBgpAgentV1=juniBgpAgentV1, PYSNMP_MODULE_ID=juniBgpAgent, juniBgpAgentV9=juniBgpAgentV9, juniBgpAgentV4=juniBgpAgentV4, juniBgpAgentV11=juniBgpAgentV11, juniBgpAgentV2=juniBgpAgentV2, juniBgpAgentV3=juniBgpAgentV3, juniBgpAgent=juniBgpAgent, juniBgpAgentV8=juniBgpAgentV8)
