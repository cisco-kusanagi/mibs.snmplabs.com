#
# PySNMP MIB module RADLAN-SWPACKAGEVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SWPACKAGEVERSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:49:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ModuleIdentity, IpAddress, MibIdentifier, Unsigned32, iso, Counter32, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ModuleIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "iso", "Counter32", "ObjectIdentity", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlSwPackageVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 67))
rlSwPackageVersion.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSwPackageVersion.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSwPackageVersion.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSwPackageVersion.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlSwPackageVersion.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlSwPackageVersion.setDescription('This private MIB module defines SW package version private MIBs.')
rlSwPackageVersionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 67, 1), )
if mibBuilder.loadTexts: rlSwPackageVersionTable.setStatus('current')
if mibBuilder.loadTexts: rlSwPackageVersionTable.setDescription('The table listing the current versions of packages that are included in the running software.')
rlSwPackageVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 67, 1, 1), ).setIndexNames((1, "RADLAN-SWPACKAGEVERSION-MIB", "rlSwPackageVersionName"))
if mibBuilder.loadTexts: rlSwPackageVersionEntry.setStatus('current')
if mibBuilder.loadTexts: rlSwPackageVersionEntry.setDescription('The row definition for this table.')
rlSwPackageVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionName.setStatus('current')
if mibBuilder.loadTexts: rlSwPackageVersionName.setDescription('The Package name.')
rlSwPackageVersionVesrion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionVesrion.setStatus('current')
if mibBuilder.loadTexts: rlSwPackageVersionVesrion.setDescription('The Package version.')
mibBuilder.exportSymbols("RADLAN-SWPACKAGEVERSION-MIB", rlSwPackageVersion=rlSwPackageVersion, rlSwPackageVersionTable=rlSwPackageVersionTable, rlSwPackageVersionName=rlSwPackageVersionName, rlSwPackageVersionEntry=rlSwPackageVersionEntry, rlSwPackageVersionVesrion=rlSwPackageVersionVesrion, PYSNMP_MODULE_ID=rlSwPackageVersion)
