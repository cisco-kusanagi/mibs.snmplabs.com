#
# PySNMP MIB module CISCO-IGMP-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IGMP-FILTER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, iso, Unsigned32, TimeTicks, Integer32, IpAddress, MibIdentifier, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Unsigned32", "TimeTicks", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIgmpFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 331))
ciscoIgmpFilterCapability.setRevisions(('2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setOrganization('Cisco Systems, Inc.')
cIgmpFilterCapCatOSV07R0101Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 331, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setProductRelease('Cisco CatOS 7.1(1) on Catalyst 4000/4500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setStatus('current')
mibBuilder.exportSymbols("CISCO-IGMP-FILTER-CAPABILITY", cIgmpFilterCapCatOSV07R0101Cat4k=cIgmpFilterCapCatOSV07R0101Cat4k, PYSNMP_MODULE_ID=ciscoIgmpFilterCapability, ciscoIgmpFilterCapability=ciscoIgmpFilterCapability)
