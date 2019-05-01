#
# PySNMP MIB module APPIAN-TRUNK-SHARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-TRUNK-SHARE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acTrunks, AcAdminStatus = mibBuilder.importSymbols("APPIAN-SMI-MIB", "acTrunks", "AcAdminStatus")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Integer32, NotificationType, Gauge32, Counter32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Unsigned32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Integer32", "NotificationType", "Gauge32", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Unsigned32", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acTrunksShare = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1))
acTrunksShare.setRevisions(('1900-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acTrunksShare.setRevisionsDescriptions(('Draft engineering version. Not for release.',))
if mibBuilder.loadTexts: acTrunksShare.setLastUpdated('0002130000Z')
if mibBuilder.loadTexts: acTrunksShare.setOrganization('Appian Communications, Inc.')
if mibBuilder.loadTexts: acTrunksShare.setContactInfo('Douglas Theriault')
if mibBuilder.loadTexts: acTrunksShare.setDescription('Appian Communications Common trunking MIBs.')
class AcTrunkTimeSlots(TextualConvention, OctetString):
    description = 'List of timeslots bound to a trunk.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 28)

acTrunkSharedTable = MibTable((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1), )
if mibBuilder.loadTexts: acTrunkSharedTable.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedTable.setDescription('The trunking provisioning table. Records in this table are created by management action and not by the OSAP.')
acTrunkSharedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1), ).setIndexNames((0, "APPIAN-TRUNK-SHARE-MIB", "acTrunkSharedIndex"))
if mibBuilder.loadTexts: acTrunkSharedEntry.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedEntry.setDescription('A row within the trunk provisioning shared table.')
acTrunkSharedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acTrunkSharedIndex.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedIndex.setDescription('An index key that uniquely identifies a row in the trunk table.')
acTrunkSharedAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 2), AcAdminStatus().clone('inactivate')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedAdminStatus.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedAdminStatus.setDescription('Controls the operational status of the trunk ')
acTrunkSharedName = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedName.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedName.setDescription('The user assigned ASCII name for this trunk.')
acTrunkSharedIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedIdentifier.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedIdentifier.setDescription('The user assigned numeric ID for this trunk')
acTrunkSharedDataProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 0), ("frame-relay", 1), ("mfr", 2), ("ppp", 3), ("mlppp", 4), ("tls", 5))).clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedDataProtocol.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedDataProtocol.setDescription('Defines the WAN protocol running over this trunk.')
acTrunkSharedTimeslotList = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 6), AcTrunkTimeSlots()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkSharedTimeslotList.setStatus('current')
if mibBuilder.loadTexts: acTrunkSharedTimeslotList.setDescription('List of timeslots bound this this trunk (Logical ports map to timeslots).')
mibBuilder.exportSymbols("APPIAN-TRUNK-SHARE-MIB", acTrunkSharedAdminStatus=acTrunkSharedAdminStatus, acTrunkSharedDataProtocol=acTrunkSharedDataProtocol, PYSNMP_MODULE_ID=acTrunksShare, acTrunkSharedTimeslotList=acTrunkSharedTimeslotList, acTrunksShare=acTrunksShare, acTrunkSharedIndex=acTrunkSharedIndex, acTrunkSharedEntry=acTrunkSharedEntry, acTrunkSharedTable=acTrunkSharedTable, acTrunkSharedName=acTrunkSharedName, AcTrunkTimeSlots=AcTrunkTimeSlots, acTrunkSharedIdentifier=acTrunkSharedIdentifier)
