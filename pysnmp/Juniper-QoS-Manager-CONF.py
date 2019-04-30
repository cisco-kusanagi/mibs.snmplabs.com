#
# PySNMP MIB module Juniper-QoS-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-QoS-Manager-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Bits, Counter64, NotificationType, ObjectIdentity, TimeTicks, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, iso, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "iso", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniQosManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50))
juniQosManagerAgent.setRevisions(('2004-01-26 14:43', '2003-05-08 18:55', '2002-09-27 18:03', '2001-12-06 16:09',))
if mibBuilder.loadTexts: juniQosManagerAgent.setLastUpdated('200401261443Z')
if mibBuilder.loadTexts: juniQosManagerAgent.setOrganization('Juniper Networks, Inc.')
juniQosManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV1 = juniQosManagerAgentV1.setProductRelease('Version 1 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component was supported in JUNOSe 4.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV1 = juniQosManagerAgentV1.setStatus('obsolete')
juniQosManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV2 = juniQosManagerAgentV2.setProductRelease('Version 2 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component was supported in JUNOSe 5.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV2 = juniQosManagerAgentV2.setStatus('obsolete')
juniQosManagerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV3 = juniQosManagerAgentV3.setProductRelease('Version 3 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component was supported in JUNOSe 5.1 and\n        subsequent 5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV3 = juniQosManagerAgentV3.setStatus('obsolete')
juniQosManagerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV4 = juniQosManagerAgentV4.setProductRelease('Version 4 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component is supported in JUNOSe 6.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV4 = juniQosManagerAgentV4.setStatus('current')
mibBuilder.exportSymbols("Juniper-QoS-Manager-CONF", juniQosManagerAgentV1=juniQosManagerAgentV1, juniQosManagerAgentV3=juniQosManagerAgentV3, PYSNMP_MODULE_ID=juniQosManagerAgent, juniQosManagerAgentV2=juniQosManagerAgentV2, juniQosManagerAgent=juniQosManagerAgent, juniQosManagerAgentV4=juniQosManagerAgentV4)
