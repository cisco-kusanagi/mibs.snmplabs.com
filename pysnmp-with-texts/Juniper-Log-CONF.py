#
# PySNMP MIB module Juniper-Log-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Log-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, Counter64, ModuleIdentity, iso, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter32, Bits, Gauge32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ModuleIdentity", "iso", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniLogAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26))
juniLogAgent.setRevisions(('2002-09-06 16:54', '2001-03-28 22:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniLogAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniLogAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniLogAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniLogAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniLogAgent.setDescription('The agent capabilities definitions for the logging managment component of the SNMP agent in the Juniper E-series family of products.')
juniLogAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV1 = juniLogAgentV1.setProductRelease('Version 1 of the logging managment component of the JUNOSe SNMP agent.\n        This version of the logging managment component was supported in JUNOSe\n        1.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV1 = juniLogAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniLogAgentV1.setDescription('The MIB supported by the SNMP agent for the logging managment application in JUNOSe. These capabilities became obsolete when the single syslog destination was replaced with a table of syslog destinations and the syslog facility was added.')
juniLogAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV2 = juniLogAgentV2.setProductRelease('Version 2 of the logging managment component of the JUNOSe SNMP agent.\n        This version of the logging managment component is supported in JUNOSe\n        2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLogAgentV2 = juniLogAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniLogAgentV2.setDescription('The MIB supported by the SNMP agent for the logging managment application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Log-CONF", juniLogAgentV1=juniLogAgentV1, juniLogAgentV2=juniLogAgentV2, juniLogAgent=juniLogAgent, PYSNMP_MODULE_ID=juniLogAgent)
