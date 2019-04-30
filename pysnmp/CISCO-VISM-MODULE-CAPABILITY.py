#
# PySNMP MIB module CISCO-VISM-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-MODULE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, TimeTicks, NotificationType, iso, Counter32, IpAddress, MibIdentifier, Integer32, Bits, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "NotificationType", "iso", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "Bits", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 458))
ciscoVismModuleCapability.setRevisions(('2005-10-18 00:00',))
if mibBuilder.loadTexts: ciscoVismModuleCapability.setLastUpdated('200510180000Z')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setOrganization('Cisco Systems, Inc.')
cVismModuleCapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 458, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismModuleCapabilityV3325 = cVismModuleCapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismModuleCapabilityV3325 = cVismModuleCapabilityV3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-MODULE-CAPABILITY", ciscoVismModuleCapability=ciscoVismModuleCapability, cVismModuleCapabilityV3325=cVismModuleCapabilityV3325, PYSNMP_MODULE_ID=ciscoVismModuleCapability)
