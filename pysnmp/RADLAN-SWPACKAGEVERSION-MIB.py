#
# PySNMP MIB module RADLAN-SWPACKAGEVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SWPACKAGEVERSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:41:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, NotificationType, MibIdentifier, Gauge32, Counter64, Unsigned32, ObjectIdentity, IpAddress, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlSwPackageVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 67))
rlSwPackageVersion.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSwPackageVersion.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSwPackageVersion.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSwPackageVersionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 67, 1), )
if mibBuilder.loadTexts: rlSwPackageVersionTable.setStatus('current')
rlSwPackageVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 67, 1, 1), ).setIndexNames((1, "RADLAN-SWPACKAGEVERSION-MIB", "rlSwPackageVersionName"))
if mibBuilder.loadTexts: rlSwPackageVersionEntry.setStatus('current')
rlSwPackageVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionName.setStatus('current')
rlSwPackageVersionVesrion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionVesrion.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SWPACKAGEVERSION-MIB", PYSNMP_MODULE_ID=rlSwPackageVersion, rlSwPackageVersion=rlSwPackageVersion, rlSwPackageVersionEntry=rlSwPackageVersionEntry, rlSwPackageVersionName=rlSwPackageVersionName, rlSwPackageVersionVesrion=rlSwPackageVersionVesrion, rlSwPackageVersionTable=rlSwPackageVersionTable)
