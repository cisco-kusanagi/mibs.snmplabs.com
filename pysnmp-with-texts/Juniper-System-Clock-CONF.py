#
# PySNMP MIB module Juniper-System-Clock-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-System-Clock-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, ObjectIdentity, Unsigned32, TimeTicks, NotificationType, Gauge32, Counter32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "ObjectIdentity", "Unsigned32", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSysClockAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52))
juniSysClockAgent.setRevisions(('2005-12-14 14:01', '2003-09-15 14:03', '2003-09-12 14:39', '2002-04-04 18:47',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSysClockAgent.setRevisionsDescriptions(('Added rsNtpPeerLastUpdateTime to Peer Table.', 'Replaced Unisphere names with Juniper names.', 'Added an indicator to stratum number that no stratum is set. Added traps for significant NTP state changes. Added replacement clock offset and frequency error objects with DisplaySting syntax.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSysClockAgent.setLastUpdated('200512141401Z')
if mibBuilder.loadTexts: juniSysClockAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSysClockAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSysClockAgent.setDescription('The agent capabilities definitions for the system clock component of the SNMP agent in the Juniper E-series family of products.')
juniSysClockAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV1 = juniSysClockAgentV1.setProductRelease('Version 1 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component was supported in JUNOSe 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV1 = juniSysClockAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSysClockAgentV1.setDescription('The MIB supported by the SNMP agent for the system clock application in JUNOSe. These capabilities became obsolete when NTP trap support was added.')
juniSysClockAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV2 = juniSysClockAgentV2.setProductRelease('Version 2 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component was supported in early JUNOSe 4.1\n        and 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV2 = juniSysClockAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniSysClockAgentV2.setDescription('The MIB supported by the SNMP agent for the system clock application in JUNOSe. These capabilities became obsolete when new frequency and offset error obejects support were added.')
juniSysClockAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV3 = juniSysClockAgentV3.setProductRelease('Version 3 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component is supported in JUNOSe 4.1.2,\n        5.0.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV3 = juniSysClockAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniSysClockAgentV3.setDescription('The MIB supported by the SNMP agent for the system clock application in JUNOSe.')
juniSysClockAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV4 = juniSysClockAgentV4.setProductRelease('Version 4 of the system clock component of the JUNOSe SNMP agent.  This\n        version of the system clock component is supported in JUNOSe 7.0 and \n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSysClockAgentV4 = juniSysClockAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniSysClockAgentV4.setDescription('The MIB supported by the SNMP agent for the system clock application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-System-Clock-CONF", juniSysClockAgentV3=juniSysClockAgentV3, juniSysClockAgentV1=juniSysClockAgentV1, juniSysClockAgent=juniSysClockAgent, PYSNMP_MODULE_ID=juniSysClockAgent, juniSysClockAgentV2=juniSysClockAgentV2, juniSysClockAgentV4=juniSysClockAgentV4)
