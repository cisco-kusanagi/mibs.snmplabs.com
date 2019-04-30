#
# PySNMP MIB module CISCO-VSI-CONTROLLER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VSI-CONTROLLER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, TimeTicks, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Counter32, Unsigned32, iso, ModuleIdentity, NotificationType, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Counter32", "Unsigned32", "iso", "ModuleIdentity", "NotificationType", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVsiControllerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoVsiControllerCapability.setRevisions(('2002-05-02 00:00',))
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setLastUpdated('200205020000Z')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setOrganization('Cisco Systems, Inc.')
ciscoVsiControllerCapabilityVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setStatus('current')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-CAPABILITY", ciscoVsiControllerCapabilityVR200=ciscoVsiControllerCapabilityVR200, ciscoVsiControllerCapability=ciscoVsiControllerCapability, PYSNMP_MODULE_ID=ciscoVsiControllerCapability)
