#
# PySNMP MIB module IANA-STORAGE-MEDIA-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-STORAGE-MEDIA-TYPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, Unsigned32, ModuleIdentity, iso, TimeTicks, Integer32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, NotificationType, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Unsigned32", "ModuleIdentity", "iso", "TimeTicks", "Integer32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "NotificationType", "ObjectIdentity", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaStorageMediaTypeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 237))
ianaStorageMediaTypeMIB.setRevisions(('2015-10-12 00:00',))
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setLastUpdated('201510120000Z')
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setOrganization('IANA')
class IANAStorageMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("hardDisk", 3), ("opticalDisk", 4), ("floppyDisk", 5))

mibBuilder.exportSymbols("IANA-STORAGE-MEDIA-TYPE-MIB", IANAStorageMediaType=IANAStorageMediaType, ianaStorageMediaTypeMIB=ianaStorageMediaTypeMIB, PYSNMP_MODULE_ID=ianaStorageMediaTypeMIB)
