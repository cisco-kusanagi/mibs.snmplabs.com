#
# PySNMP MIB module CISCO-WAN-ATM-CONN-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-CONN-STAT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, MibIdentifier, iso, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, IpAddress, Counter32, Counter64, Integer32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "iso", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "IpAddress", "Counter32", "Counter64", "Integer32", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanAtmConnStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoWanAtmConnStatCapability.setRevisions(('2003-04-08 00:00', '2001-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setRevisionsDescriptions(('Added cwacsCapabilityAxsmxgV4R00 for 10 Gig. AXSM Module (AXSM-XG).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setLastUpdated('200304080000Z')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setDescription('The Agent Capabilities for CISCO-WAN-ATM-CONN-STAT-MIB for different Service Modules in in MGX8850 Series. - The cwaConnStatCapabilityAxsmV21R60 is for ATM Switch Service Module(AXSM). - The cwAtmConnStatCapabilityAxsmeV2R0170 is for Enhanced AXSM(AXSM-E) module. - The cwAtmConnStatCapabilityPxm1eV2R300 is for PXM1-E module')
cwaConnStatCapabilityAxsmV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setStatus('current')
if mibBuilder.loadTexts: cwaConnStatCapabilityAxsmV21R60.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities for ATM Switch Service Module(AXSM).')
cwAtmConnStatCapabilityAxsmeV2R0170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setProductRelease('MGX8850 Release 2.1.70')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnStatCapabilityAxsmeV2R0170.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities for Enhanced AXSM(AXSM-E) Module.')
cwAtmConnStatCapabilityPxm1eV2R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnStatCapabilityPxm1eV2R300.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities for PXM1-E Module.')
cwacsCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setStatus('current')
if mibBuilder.loadTexts: cwacsCapabilityAxsmxgV4R00.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities for 10 Gig. AXSM Module (AXSM-XG).')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-STAT-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanAtmConnStatCapability, ciscoWanAtmConnStatCapability=ciscoWanAtmConnStatCapability, cwaConnStatCapabilityAxsmV21R60=cwaConnStatCapabilityAxsmV21R60, cwAtmConnStatCapabilityPxm1eV2R300=cwAtmConnStatCapabilityPxm1eV2R300, cwacsCapabilityAxsmxgV4R00=cwacsCapabilityAxsmxgV4R00, cwAtmConnStatCapabilityAxsmeV2R0170=cwAtmConnStatCapabilityAxsmeV2R0170)
