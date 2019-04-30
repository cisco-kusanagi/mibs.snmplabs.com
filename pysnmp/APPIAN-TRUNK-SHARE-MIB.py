#
# PySNMP MIB module APPIAN-TRUNK-SHARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-TRUNK-SHARE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AcAdminStatus, acTrunks = mibBuilder.importSymbols("APPIAN-SMI-MIB", "AcAdminStatus", "acTrunks")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, MibIdentifier, Integer32, Bits, iso, NotificationType, Counter32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "iso", "NotificationType", "Counter32", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acTrunksShare = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1))
acTrunksShare.setRevisions(('1900-02-13 00:00',))
if mibBuilder.loadTexts: acTrunksShare.setLastUpdated('0002130000Z')
if mibBuilder.loadTexts: acTrunksShare.setOrganization('Appian Communications, Inc.')
class AcTrunkTimeSlots(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 28)

acTrunkSharedTable = MibTable((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1), )
if mibBuilder.loadTexts: acTrunkSharedTable.setStatus('current')
acTrunkSharedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1), ).setIndexNames((0, "APPIAN-TRUNK-SHARE-MIB", "acTrunkSharedIndex"))
if mibBuilder.loadTexts: acTrunkSharedEntry.setStatus('current')
acTrunkSharedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acTrunkSharedIndex.setStatus('current')
acTrunkSharedAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 2), AcAdminStatus().clone('inactivate')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedAdminStatus.setStatus('current')
acTrunkSharedName = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedName.setStatus('current')
acTrunkSharedIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedIdentifier.setStatus('current')
acTrunkSharedDataProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 0), ("frame-relay", 1), ("mfr", 2), ("ppp", 3), ("mlppp", 4), ("tls", 5))).clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedDataProtocol.setStatus('current')
acTrunkSharedTimeslotList = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 6), AcTrunkTimeSlots()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedTimeslotList.setStatus('current')
mibBuilder.exportSymbols("APPIAN-TRUNK-SHARE-MIB", acTrunkSharedName=acTrunkSharedName, PYSNMP_MODULE_ID=acTrunksShare, acTrunkSharedAdminStatus=acTrunkSharedAdminStatus, acTrunkSharedIdentifier=acTrunkSharedIdentifier, acTrunkSharedIndex=acTrunkSharedIndex, acTrunkSharedTable=acTrunkSharedTable, acTrunkSharedTimeslotList=acTrunkSharedTimeslotList, AcTrunkTimeSlots=AcTrunkTimeSlots, acTrunkSharedDataProtocol=acTrunkSharedDataProtocol, acTrunksShare=acTrunksShare, acTrunkSharedEntry=acTrunkSharedEntry)
