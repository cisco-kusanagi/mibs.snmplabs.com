#
# PySNMP MIB module CISCO-IMAGE-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Gauge32, Unsigned32, ObjectIdentity, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, TimeTicks, Integer32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Gauge32", "Unsigned32", "ObjectIdentity", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "TimeTicks", "Integer32", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 455))
ciscoImageTc.setRevisions(('2005-01-12 00:00',))
if mibBuilder.loadTexts: ciscoImageTc.setLastUpdated('200501120000Z')
if mibBuilder.loadTexts: ciscoImageTc.setOrganization('Cisco Systems, Inc.')
class CeImageInstallableStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("active", 1), ("pendingInstall", 2), ("pendingRemoval", 3), ("installPendingReload", 4), ("removedPendingReload", 5), ("installPendingReloadPendingRemoval", 6), ("removedPendingReloadPendingInstall", 7), ("pruned", 8), ("inactive", 9))

class CeImageInstallableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("base", 1), ("patch", 2), ("script", 3), ("package", 4), ("compositePackage", 5), ("softwareMaintenanceUpgrade", 6))

mibBuilder.exportSymbols("CISCO-IMAGE-TC", CeImageInstallableStatus=CeImageInstallableStatus, CeImageInstallableType=CeImageInstallableType, ciscoImageTc=ciscoImageTc, PYSNMP_MODULE_ID=ciscoImageTc)
