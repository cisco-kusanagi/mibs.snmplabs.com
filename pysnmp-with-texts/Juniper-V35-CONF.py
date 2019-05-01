#
# PySNMP MIB module Juniper-V35-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-V35-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, Integer32, MibIdentifier, Counter32, Gauge32, NotificationType, IpAddress, ModuleIdentity, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "Counter32", "Gauge32", "NotificationType", "IpAddress", "ModuleIdentity", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniV35Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54))
juniV35Agent.setRevisions(('2002-09-06 16:54', '2002-01-25 21:43',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniV35Agent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniV35Agent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniV35Agent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniV35Agent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniV35Agent.setDescription('The agent capabilities definitions for the X.21/V.35 server component of the SNMP agent in the Juniper E-series family of products.')
juniV35AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniV35AgentV1 = juniV35AgentV1.setProductRelease('Version 1 of the X.21/V.35 component of the JUNOSe SNMP agent.  This\n        version of the X.21/V.35 component is supported in JUNOSe 4.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniV35AgentV1 = juniV35AgentV1.setStatus('current')
if mibBuilder.loadTexts: juniV35AgentV1.setDescription('The MIB supported by the SNMP agent for the X.21/V.35 application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-V35-CONF", juniV35AgentV1=juniV35AgentV1, PYSNMP_MODULE_ID=juniV35Agent, juniV35Agent=juniV35Agent)
