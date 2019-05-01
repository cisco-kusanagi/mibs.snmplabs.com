#
# PySNMP MIB module CISCO-WAN-VISM-T38-FAX-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-T38-FAX-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, IpAddress, MibIdentifier, Integer32, iso, ModuleIdentity, TimeTicks, Bits, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Integer32", "iso", "ModuleIdentity", "TimeTicks", "Bits", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cwVismT38FaxCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 335))
cwVismT38FaxCapability.setRevisions(('2001-08-05 00:00', '2002-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismT38FaxCapability.setRevisionsDescriptions(('Initial version of this MIB module', ' t38FaxInfoFieldSize variation was modified. t38HsDataPacketSize variation was added. t38LsDataRedundancy variation was modified. t38HsDataRedundancy variation was modified. t38ErrCorrection variation was added. t38NSFCountryCode variation was modified. t38NSFVendorCode variation was added. t38Redundancy variation was added. ',))
if mibBuilder.loadTexts: cwVismT38FaxCapability.setLastUpdated('200206010000Z')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setDescription('The Agent Capabilities for CISCO-WAN-T38-FAXRELAY-MIB.')
cwVismT38FaxCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setProductRelease('VISM Release3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismT38FaxCapabilityV2R00.setDescription('CISCO-WAN-T38-FAXRELAY-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-T38-FAX-CAPABILITY", PYSNMP_MODULE_ID=cwVismT38FaxCapability, cwVismT38FaxCapability=cwVismT38FaxCapability, cwVismT38FaxCapabilityV2R00=cwVismT38FaxCapabilityV2R00)
