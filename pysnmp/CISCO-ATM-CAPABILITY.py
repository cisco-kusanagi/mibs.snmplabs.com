#
# PySNMP MIB module CISCO-ATM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, TimeTicks, IpAddress, iso, ModuleIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, ObjectIdentity, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "IpAddress", "iso", "ModuleIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAtmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoAtmCapability.setRevisions(('2002-06-12 00:00',))
if mibBuilder.loadTexts: ciscoAtmCapability.setLastUpdated('200206120000Z')
if mibBuilder.loadTexts: ciscoAtmCapability.setOrganization('Cisco Systems, Inc.')
ciscoAtmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmCapability, ciscoAtmCapability=ciscoAtmCapability, ciscoAtmCapabilityV2R00=ciscoAtmCapabilityV2R00)
