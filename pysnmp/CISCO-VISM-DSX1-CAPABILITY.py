#
# PySNMP MIB module CISCO-VISM-DSX1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-DSX1-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, Counter32, MibIdentifier, Integer32, ModuleIdentity, IpAddress, TimeTicks, iso, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "Counter32", "MibIdentifier", "Integer32", "ModuleIdentity", "IpAddress", "TimeTicks", "iso", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismDsx1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 450))
ciscoVismDsx1Capability.setRevisions(('2005-09-26 00:00',))
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setOrganization('Cisco Systems, Inc.')
cVismDsx1CapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 450, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-DSX1-CAPABILITY", PYSNMP_MODULE_ID=ciscoVismDsx1Capability, ciscoVismDsx1Capability=ciscoVismDsx1Capability, cVismDsx1CapabilityV3325=cVismDsx1CapabilityV3325)
