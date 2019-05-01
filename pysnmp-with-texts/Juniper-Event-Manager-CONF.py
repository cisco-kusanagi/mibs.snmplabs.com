#
# PySNMP MIB module Juniper-Event-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Event-Manager-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, TimeTicks, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Gauge32, Unsigned32, ObjectIdentity, MibIdentifier, Counter64, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter64", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniEventManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62))
juniEventManagerAgent.setRevisions(('2003-10-30 14:43', '2003-05-12 14:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniEventManagerAgent.setRevisionsDescriptions(('DISMAN-EVENT-MIB: Added support for existence and boolean triggers. Added support for multiple agent wildcarding. Added support for event Set capabilities. Juniper-DISMAN-EVENT-MIB: Initial release for the proprietary Event Manager MIB.', 'The initial release of this management information module. DISMAN-EVENT-MIB: Added partial support for the draft-ietf-disman-event-mib-v2-01 version (enhancements to RFC 2981): Supports threshold triggers for absolute and delta sampling. Does not support existence or boolean triggers. Does not support wildcarding. Does not support event Set capabilities.',))
if mibBuilder.loadTexts: juniEventManagerAgent.setLastUpdated('200310301443Z')
if mibBuilder.loadTexts: juniEventManagerAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniEventManagerAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniEventManagerAgent.setDescription('The agent capabilities definitions for the Event Manager component of the SNMP agent in the Juniper E-series family of products.')
juniEventManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV1 = juniEventManagerAgentV1.setProductRelease('Version 1 of the Event Manager component of the JUNOSe SNMP agent.\n        This version of the Event Manager component was supported in JUNOSe 5.1\n        and 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV1 = juniEventManagerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniEventManagerAgentV1.setDescription('The MIBs supported by the SNMP agent for the Event Manager application in JUNOSe. These capabilities became obsolete when support was added for existence and boolean triggers, multiple agent wildcarding, and event Set capabilities.')
juniEventManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV2 = juniEventManagerAgentV2.setProductRelease('Version 2 of the Event Manager component of the JUNOSe SNMP agent.\n        This version of the Event Manager component is supported in JUNOSe 5.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV2 = juniEventManagerAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniEventManagerAgentV2.setDescription('The MIBs supported by the SNMP agent for the Event Manager application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Event-Manager-CONF", juniEventManagerAgent=juniEventManagerAgent, PYSNMP_MODULE_ID=juniEventManagerAgent, juniEventManagerAgentV1=juniEventManagerAgentV1, juniEventManagerAgentV2=juniEventManagerAgentV2)
