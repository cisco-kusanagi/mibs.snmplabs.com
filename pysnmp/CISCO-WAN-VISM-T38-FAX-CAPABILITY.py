#
# PySNMP MIB module CISCO-WAN-VISM-T38-FAX-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-T38-FAX-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, Integer32, Bits, IpAddress, MibIdentifier, Unsigned32, TimeTicks, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "Integer32", "Bits", "IpAddress", "MibIdentifier", "Unsigned32", "TimeTicks", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cwVismT38FaxCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 335))
cwVismT38FaxCapability.setRevisions(('2001-08-05 00:00', '2002-06-01 00:00',))
if mibBuilder.loadTexts: cwVismT38FaxCapability.setLastUpdated('200206010000Z')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setOrganization('Cisco Systems, Inc.')
cwVismT38FaxCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setProductRelease('VISM Release3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-T38-FAX-CAPABILITY", cwVismT38FaxCapability=cwVismT38FaxCapability, cwVismT38FaxCapabilityV2R00=cwVismT38FaxCapabilityV2R00, PYSNMP_MODULE_ID=cwVismT38FaxCapability)
