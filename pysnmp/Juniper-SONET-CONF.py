#
# PySNMP MIB module Juniper-SONET-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SONET-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, ModuleIdentity, iso, TimeTicks, Bits, NotificationType, Unsigned32, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "ModuleIdentity", "iso", "TimeTicks", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSonetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40))
juniSonetAgent.setRevisions(('2005-09-15 20:26', '2003-07-16 17:22', '2003-01-31 20:09', '2002-04-09 23:44', '2002-02-04 21:35', '2001-04-03 22:35',))
if mibBuilder.loadTexts: juniSonetAgent.setLastUpdated('200509152026Z')
if mibBuilder.loadTexts: juniSonetAgent.setOrganization('Juniper Networks, Inc.')
juniSonetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV1 = juniSonetAgentV1.setProductRelease('Version 1 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV1 = juniSonetAgentV1.setStatus('obsolete')
juniSonetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV2 = juniSonetAgentV2.setProductRelease('Version 2 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV2 = juniSonetAgentV2.setStatus('obsolete')
juniSonetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV3 = juniSonetAgentV3.setProductRelease('Version 3 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 3.0 and 3.1\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV3 = juniSonetAgentV3.setStatus('obsolete')
juniSonetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV4 = juniSonetAgentV4.setProductRelease('Version 4 of the SONET component of the JUNOSe SNMP agent.  This\n        version of the SONET component was supported in JUNOSe 3.2 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetAgentV4 = juniSonetAgentV4.setStatus('obsolete')
juniSonetBasicAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5))
juniSonetBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV1 = juniSonetBasicAgentV1.setProductRelease('Version 1 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component was supported in JUNOSe 3.3 and subsequent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV1 = juniSonetBasicAgentV1.setStatus('obsolete')
juniSonetBasicAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV2 = juniSonetBasicAgentV2.setProductRelease('Version 2 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component was supported in JUNOSe 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV2 = juniSonetBasicAgentV2.setStatus('obsolete')
juniSonetBasicAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV3 = juniSonetBasicAgentV3.setProductRelease('Version 3 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV3 = juniSonetBasicAgentV3.setStatus('obsolete')
juniSonetBasicAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV4 = juniSonetBasicAgentV4.setProductRelease('Version 4 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component is supported in JUNOSe 5.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV4 = juniSonetBasicAgentV4.setStatus('obsolete')
juniSonetBasicAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV5 = juniSonetBasicAgentV5.setProductRelease('Version 5 of the basic SONET component of the JUNOSe SNMP agent.  It\n        does not include Virtual Tributary (VT) support.  This version of the\n        basic SONET component is supported in JUNOSe 7.2 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetBasicAgentV5 = juniSonetBasicAgentV5.setStatus('current')
juniSonetVTAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6))
juniSonetVTAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetVTAgentV1 = juniSonetVTAgentV1.setProductRelease('Version 1 of the SONET VT component of the JUNOSe SNMP agent.  This\n        version of the SONET component is supported in JUNOSe 3.3 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSonetVTAgentV1 = juniSonetVTAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-SONET-CONF", juniSonetBasicAgentV2=juniSonetBasicAgentV2, juniSonetAgentV3=juniSonetAgentV3, juniSonetAgentV2=juniSonetAgentV2, juniSonetBasicAgentV4=juniSonetBasicAgentV4, juniSonetAgentV1=juniSonetAgentV1, PYSNMP_MODULE_ID=juniSonetAgent, juniSonetAgent=juniSonetAgent, juniSonetBasicAgent=juniSonetBasicAgent, juniSonetBasicAgentV3=juniSonetBasicAgentV3, juniSonetVTAgentV1=juniSonetVTAgentV1, juniSonetBasicAgentV1=juniSonetBasicAgentV1, juniSonetVTAgent=juniSonetVTAgent, juniSonetAgentV4=juniSonetAgentV4, juniSonetBasicAgentV5=juniSonetBasicAgentV5)
