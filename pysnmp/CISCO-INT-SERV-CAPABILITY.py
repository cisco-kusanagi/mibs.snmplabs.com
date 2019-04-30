#
# PySNMP MIB module CISCO-INT-SERV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-INT-SERV-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter64, IpAddress, ObjectIdentity, iso, MibIdentifier, Counter32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "ObjectIdentity", "iso", "MibIdentifier", "Counter32", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIntServCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoIntServCapability.setLastUpdated('200206210000Z')
if mibBuilder.loadTexts: ciscoIntServCapability.setOrganization('Cisco Systems, Inc.')
ciscoIntServCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-INT-SERV-CAPABILITY", ciscoIntServCapability=ciscoIntServCapability, PYSNMP_MODULE_ID=ciscoIntServCapability, ciscoIntServCapabilityVismV3R00=ciscoIntServCapabilityVismV3R00)
