#
# PySNMP MIB module CISCO-PNNI-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PNNI-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, TimeTicks, ModuleIdentity, IpAddress, Unsigned32, Bits, Integer32, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ModuleIdentity", "IpAddress", "Unsigned32", "Bits", "Integer32", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPnniCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoPnniCapability.setRevisions(('2002-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPnniCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPnniCapability.setLastUpdated('200205020000Z')
if mibBuilder.loadTexts: ciscoPnniCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPnniCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoPnniCapability.setDescription('The Agent Capabilities for PNNI-MIB.')
ciscoPnniCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniCapabilityV2R00 = ciscoPnniCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniCapabilityV2R00 = ciscoPnniCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoPnniCapabilityV2R00.setDescription('PNNI MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-PNNI-CAPABILITY", ciscoPnniCapability=ciscoPnniCapability, PYSNMP_MODULE_ID=ciscoPnniCapability, ciscoPnniCapabilityV2R00=ciscoPnniCapabilityV2R00)
