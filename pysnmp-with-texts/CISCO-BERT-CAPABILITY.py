#
# PySNMP MIB module CISCO-BERT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BERT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, ModuleIdentity, Counter32, MibIdentifier, IpAddress, TimeTicks, Unsigned32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "MibIdentifier", "IpAddress", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBertCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 274))
ciscoBertCapability.setRevisions(('2004-08-07 00:00', '2003-12-22 00:00', '2003-09-19 00:00', '2002-10-30 00:00', '2002-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBertCapability.setRevisionsDescriptions(('Modify ciscoBertCapabilityV5R015 for VXSM release 5.0.15.', 'Modify ciscoBertCapabilityV5R00 for VXSM release 5.0.0.', 'Added ciscoBertCapabilityV5R00 for VXSM release 5.0.0.', 'Added cbRowStatus support description.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBertCapability.setLastUpdated('200408070000Z')
if mibBuilder.loadTexts: ciscoBertCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBertCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoBertCapability.setDescription('The Agent Capabilities for CISCO-BERT-MIB for Cisco Products Series. - ciscoBertAxsmeCapabilityV3R00 is for Enhanced ATM Switch Service Module(AXSM-E), and Enhanced Processor Switch Module 1(PXM1E) uplink.')
ciscoBertAxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertAxsmeCapabilityV3R00 = ciscoBertAxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertAxsmeCapabilityV3R00 = ciscoBertAxsmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoBertAxsmeCapabilityV3R00.setDescription('CISCO-BERT-MIB Capabilities.')
ciscoBertCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R00 = ciscoBertCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R00 = ciscoBertCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoBertCapabilityV5R00.setDescription('CISCO-BERT-MIB capabilities for Voice Switch Service Module (VXSM) Release 5.0.0')
ciscoBertCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R015 = ciscoBertCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R015 = ciscoBertCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoBertCapabilityV5R015.setDescription('CISCO-BERT-MIB capabilities for Voice Switch Service Module (VXSM) Release 5.0.15')
mibBuilder.exportSymbols("CISCO-BERT-CAPABILITY", ciscoBertCapabilityV5R015=ciscoBertCapabilityV5R015, ciscoBertAxsmeCapabilityV3R00=ciscoBertAxsmeCapabilityV3R00, ciscoBertCapabilityV5R00=ciscoBertCapabilityV5R00, PYSNMP_MODULE_ID=ciscoBertCapability, ciscoBertCapability=ciscoBertCapability)
