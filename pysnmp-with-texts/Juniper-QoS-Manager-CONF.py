#
# PySNMP MIB module Juniper-QoS-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-QoS-Manager-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Gauge32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ModuleIdentity, Unsigned32, IpAddress, Integer32, TimeTicks, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "IpAddress", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniQosManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50))
juniQosManagerAgent.setRevisions(('2004-01-26 14:43', '2003-05-08 18:55', '2002-09-27 18:03', '2001-12-06 16:09',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniQosManagerAgent.setRevisionsDescriptions(('Added support for multiple traffic class groups.', 'Added ATM VP UID, statistics profile list, scheduler profile assured rate and QoS mode port support.', 'Replaced Unisphere names with Juniper names. Added drop profile list support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniQosManagerAgent.setLastUpdated('200401261443Z')
if mibBuilder.loadTexts: juniQosManagerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniQosManagerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniQosManagerAgent.setDescription('The agent capabilities definitions for the Quality of Service (QoS) Manager component of the SNMP agent in the Juniper E-series family of products.')
juniQosManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV1 = juniQosManagerAgentV1.setProductRelease('Version 1 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component was supported in JUNOSe 4.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV1 = juniQosManagerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniQosManagerAgentV1.setDescription('The MIB supported by the SNMP agent for the QoS Manager application in JUNOSe. These capabilities became obsolete when drop profile list support was added.')
juniQosManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV2 = juniQosManagerAgentV2.setProductRelease('Version 2 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component was supported in JUNOSe 5.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV2 = juniQosManagerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniQosManagerAgentV2.setDescription('The MIB supported by the SNMP agent for the QoS Manager application in JUNOSe. These capabilities became obsolete when ATM VP UID, statistics profile list and QoS mode port support was added.')
juniQosManagerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV3 = juniQosManagerAgentV3.setProductRelease('Version 3 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component was supported in JUNOSe 5.1 and\n        subsequent 5.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV3 = juniQosManagerAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniQosManagerAgentV3.setDescription('The MIB supported by the SNMP agent for the QoS Manager application in JUNOSe. These capabilities became obsolete when multiple traffic class group support was added.')
juniQosManagerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV4 = juniQosManagerAgentV4.setProductRelease('Version 4 of the QoS Manager component of the JUNOSe SNMP agent.  This\n        version of the QoS Manager component is supported in JUNOSe 6.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniQosManagerAgentV4 = juniQosManagerAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniQosManagerAgentV4.setDescription('The MIB supported by the SNMP agent for the QoS Manager application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-QoS-Manager-CONF", juniQosManagerAgentV2=juniQosManagerAgentV2, juniQosManagerAgent=juniQosManagerAgent, juniQosManagerAgentV1=juniQosManagerAgentV1, juniQosManagerAgentV3=juniQosManagerAgentV3, PYSNMP_MODULE_ID=juniQosManagerAgent, juniQosManagerAgentV4=juniQosManagerAgentV4)
