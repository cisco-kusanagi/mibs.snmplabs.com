#
# PySNMP MIB module TN3270E-RT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TN3270E-RT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:23:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
IANATn3270eAddrType, IANATn3270eAddress = mibBuilder.importSymbols("IANATn3270eTC-MIB", "IANATn3270eAddrType", "IANATn3270eAddress")
snanauMIB, = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, IpAddress, Bits, TimeTicks, iso, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "iso", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64")
TestAndIncr, DateAndTime, TimeStamp, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "DateAndTime", "TimeStamp", "TextualConvention", "RowStatus", "DisplayString")
tn3270eClientGroupName, tn3270eSrvrConfIndex, tn3270eResMapElementType = mibBuilder.importSymbols("TN3270E-MIB", "tn3270eClientGroupName", "tn3270eSrvrConfIndex", "tn3270eResMapElementType")
tn3270eRtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 9))
tn3270eRtMIB.setRevisions(('2006-01-13 00:00', '1998-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tn3270eRtMIB.setRevisionsDescriptions(('Removed the IMPORTing of Unsigned32 from CISCO-TC, by changing it back to be IMPORTed from SNMPv2-SMI (as in RFC 2562).', 'Initial version, published as RFC 2562.',))
if mibBuilder.loadTexts: tn3270eRtMIB.setLastUpdated('200601130000Z')
if mibBuilder.loadTexts: tn3270eRtMIB.setOrganization('TN3270E Working Group')
if mibBuilder.loadTexts: tn3270eRtMIB.setContactInfo('Kenneth White (kennethw@vnet.ibm.com) IBM Corp. - Dept. BRQA/Bldg. 501/G114 P.O. Box 12195 3039 Cornwallis RTP, NC 27709-2195 Robert Moore (remoore@us.ibm.com) IBM Corp. - Dept. BRQA/Bldg. 501/G114 P.O. Box 12195 3039 Cornwallis RTP, NC 27709-2195 (919) 254-4436')
if mibBuilder.loadTexts: tn3270eRtMIB.setDescription("This module defines a portion of the management information base (MIB) that enables monitoring of TN3270 and TN3270E clients' response times by a TN3270E server.")
tn3270eRtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 0))
tn3270eRtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 1))
tn3270eRtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3))
tn3270eRtCollCtlTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 1), )
if mibBuilder.loadTexts: tn3270eRtCollCtlTable.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlTable.setDescription('The response time monitoring collection control table, which allows a management application to control the types of response time data being collected, and the clients for which it is being collected. This table is indexed by tn3270eSrvrConfIndex and tn3270eClientGroupName imported from the TN3270E-MIB. tn3270eSrvrConfIndex indicates within a host which TN3270E server an entry applies to. tn3270eClientGroupName it identifies the set of IP clients for which response time data is being collected. The particular IP clients making up the set are identified in the tn3270eClientGroupTable in the TN3270E-MIB.')
tn3270eRtCollCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1), ).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"))
if mibBuilder.loadTexts: tn3270eRtCollCtlEntry.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlEntry.setDescription('An entry in the TN3270E response time monitoring collection control table. To handle the case of multiple TN3270E servers on the same host, the first index of this table is the tn3270eSrvrConfIndex from the TN3270E-MIB.')
tn3270eRtCollCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlType.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlType.setDescription('This object controls what types of response time data to collect, whether to summarize the data across the members of a client group or keep it individually, whether to introduce dynamic definite responses, and whether to generate traps. aggregate(0) - Aggregate response time data for the client group as a whole. If this bit is set to 0, then maintain response time data separately for each member of the client group. excludeIpComponent(1) - Do not include the IP-network component in any response times. ddr(2) - Enable dynamic definite response. average(3) - Produce an average response time based on a specified collection interval. buckets(4) - Maintain tn3270eRtDataBucket values in a corresponding tn3270eRtDataEntry, based on the bucket boundaries specified in the tn3270eRtCollCtlBucketBndry objects . traps(5) - generate the notifications specified in this MIB module. The tn3270eRtExceeded and tn3270eRtOkay notifications are generated only if average(3) is also specified.')
tn3270eRtCollCtlSPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 86400)).clone(20)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPeriod.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlSPeriod.setDescription('The number of seconds that defines the sample period. The actual interval is defined as tn3270eRtCollCtlSPeriod times tn3270eRtCollCtlSPMult. The value of this object is used only if the corresponding tn3270eRtCollCtlType has the average(3) setting.')
tn3270eRtCollCtlSPMult = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5760)).clone(30)).setUnits('period').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPMult.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlSPMult.setDescription('The sample period multiplier; this value is multiplied by the sample period, tn3270eRtCollCtlSPeriod, to determine the collection interval. Sliding-window average calculation can, if necessary, be disabled, by setting the sample period multiplier, tn3270eRtCollCtlSPMult, to 1, and setting the sample period, tn3270eRtCollCtlSPeriod, to the required collection interval. The value of this object is used only if the corresponding tn3270eRtCollCtlType has the average(3) setting.')
tn3270eRtCollCtlThreshHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshHigh.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshHigh.setDescription('The threshold for generating a tn3270eRtExceeded notification, signalling that a monitored total response time has exceeded the specified limit. A value of zero for this object suppresses generation of this notification. The value of this object is used only if the corresponding tn3270eRtCollCtlType has average(3) and traps(5) selected. A tn3270eRtExceeded notification is not generated again for a tn3270eRtDataEntry until an average response time falling below the low threshold tn3270eRtCollCtlThreshLow specified for the client group has occurred for the entry.')
tn3270eRtCollCtlThreshLow = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshLow.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshLow.setDescription('The threshold for generating a tn3270eRtOkay notification, signalling that a monitored total response time has fallen below the specified limit. A value of zero for this object suppresses generation of this notification. The value of this object is used only if the corresponding tn3270eRtCollCtlType has average(3) and traps(5) selected. A tn3270eRtOkay notification is not generated again for a tn3270eRtDataEntry until an average response time exceeding the high threshold tn3270eRtCollCtlThreshHigh specified for the client group has occurred for the entry.')
tn3270eRtCollCtlIdleCount = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 7), Unsigned32().clone(1)).setUnits('transactions').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlIdleCount.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlIdleCount.setDescription('The value of this object is used to determine whether a sample that yields an average response time exceeding the value of tn3270eRtCollCtlThreshHigh was a statistically valid one. If the following statement is true, then the sample was statistically valid, and so a tn3270eRtExceeded notification should be generated: AvgCountTrans * ((AvgRt/ThreshHigh - 1) ** 2) >= IdleCount This comparison is done only if the corresponding tn3270eRtCollCtlType has average(3) and traps(5) selected.')
tn3270eRtCollCtlBucketBndry1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 8), Unsigned32().clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry1.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry1.setDescription('The value of this object defines the range of transaction response times counted in the Tn3270eRtDataBucket1Rts object: those less than or equal to this value.')
tn3270eRtCollCtlBucketBndry2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 9), Unsigned32().clone(20)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry2.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry2.setDescription('The value of this object, together with that of the tn3270eRtCollCtlBucketBndry1 object, defines the range of transaction response times counted in the Tn3270eRtDataBucket2Rts object: those greater than the value of the tn3270eRtCollCtlBucketBndry1 object, and less than or equal to the value of this object.')
tn3270eRtCollCtlBucketBndry3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 10), Unsigned32().clone(50)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry3.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry3.setDescription('The value of this object, together with that of the tn3270eRtCollCtlBucketBndry2 object, defines the range of transaction response times counted in the Tn3270eRtDataBucket3Rts object: those greater than the value of the tn3270eRtCollCtlBucketBndry2 object, and less than or equal to the value of this object.')
tn3270eRtCollCtlBucketBndry4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 11), Unsigned32().clone(100)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry4.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry4.setDescription('The value of this object, together with that of the tn3270eRtCollCtlBucketBndry3 object, defines the range of transaction response times counted in the Tn3270eRtDataBucket4Rts object: those greater than the value of the tn3270eRtCollCtlBucketBndry3 object, and less than or equal to the value of this object. The value of this object also defines the range of transaction response times counted in the Tn3270eRtDataBucket5Rts object: those greater than the value of this object.')
tn3270eRtCollCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlRowStatus.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollCtlRowStatus.setDescription('This object allows entries to be created and deleted in the tn3270eRtCollCtlTable. An entry in this table is deleted by setting this object to destroy(6). Deleting an entry in this table has the side-effect of removing all entries from the tn3270eRtDataTable that are associated with the entry being deleted.')
tn3270eRtDataTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 2), )
if mibBuilder.loadTexts: tn3270eRtDataTable.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataTable.setDescription('The response time data table. Entries in this table are created based on entries in the tn3270eRtCollCtlTable.')
tn3270eRtDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1), ).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddrType"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddress"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientPort"))
if mibBuilder.loadTexts: tn3270eRtDataEntry.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataEntry.setDescription('Entries in this table are created based upon the tn3270eRtCollCtlTable. When the corresponding tn3270eRtCollCtlType has aggregate(0) specified, a single entry is created in this table, with a tn3270eRtDataClientAddrType of unknown(0), a zero-length octet string value for tn3270eRtDataClientAddress, and a tn3270eRtDataClientPort value of 0. When aggregate(0) is not specified, a separate entry is created for each client in the group. Note that the following objects defined within an entry in this table can wrap: tn3270eRtDataTotalRts tn3270eRtDataTotalIpRts tn3270eRtDataCountTrans tn3270eRtDataCountDrs tn3270eRtDataElapsRnTrpSq tn3270eRtDataElapsIpRtSq tn3270eRtDataBucket1Rts tn3270eRtDataBucket2Rts tn3270eRtDataBucket3Rts tn3270eRtDataBucket4Rts tn3270eRtDataBucket5Rts')
tn3270eRtDataClientAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 1), IANATn3270eAddrType())
if mibBuilder.loadTexts: tn3270eRtDataClientAddrType.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataClientAddrType.setDescription('Indicates the type of address represented by the value of tn3270eRtDataClientAddress. The value unknown(0) is used if aggregate data is being collected for the client group.')
tn3270eRtDataClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 2), IANATn3270eAddress())
if mibBuilder.loadTexts: tn3270eRtDataClientAddress.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataClientAddress.setDescription('Contains the IP address of the TN3270 client being monitored. A zero-length octet string is used if aggregate data is being collected for the client group.')
tn3270eRtDataClientPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: tn3270eRtDataClientPort.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataClientPort.setDescription('Contains the client port number of the TN3270 client being monitored. The value 0 is used if aggregate data is being collected for the client group, or if the tn3270eRtDataClientAddrType identifies an address type that does not support ports.')
tn3270eRtDataAvgRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 4), Gauge32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgRt.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataAvgRt.setDescription('The average total response time measured over the last collection interval.')
tn3270eRtDataAvgIpRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 5), Gauge32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgIpRt.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataAvgIpRt.setDescription('The average IP response time measured over the last collection interval.')
tn3270eRtDataAvgCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 6), Gauge32()).setUnits('transactions').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgCountTrans.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataAvgCountTrans.setDescription('The sliding transaction count used for calculating the values of the tn3270eRtDataAvgRt and tn3270eRtDataAvgIpRt objects. The actual transaction count is available in the tn3270eRtDataCountTrans object. The initial value of this object, before any averages have been calculated, is 0.')
tn3270eRtDataIntTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataIntTimeStamp.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataIntTimeStamp.setDescription('The date and time of the last interval that tn3270eRtDataAvgRt, tn3270eRtDataAvgIpRt, and tn3270eRtDataAvgCountTrans were calculated. Prior to the calculation of the first interval averages, this object returns the value 0x0000000000000000000000. When this value is returned, the remaining objects in the entry have no significance.')
tn3270eRtDataTotalRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 8), Counter32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalRts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataTotalRts.setDescription('The count of the total response times collected. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataTotalIpRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 9), Counter32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalIpRts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataTotalIpRts.setDescription('The count of the total IP-network response times collected. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 10), Counter32()).setUnits('transactions').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountTrans.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataCountTrans.setDescription('The count of the total number of transactions detected. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataCountDrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 11), Counter32()).setUnits('definite responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountDrs.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataCountDrs.setDescription('The count of the total number of definite responses detected. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataElapsRndTrpSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 12), Unsigned32()).setUnits('tenths of seconds squared').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsRndTrpSq.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataElapsRndTrpSq.setDescription('The sum of the elapsed round trip time squared. The sum of the squares is kept in order to enable calculation of a variance.')
tn3270eRtDataElapsIpRtSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 13), Unsigned32()).setUnits('tenths of seconds squared').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsIpRtSq.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataElapsIpRtSq.setDescription('The sum of the elapsed IP round trip time squared. The sum of the squares is kept in order to enable calculation of a variance.')
tn3270eRtDataBucket1Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket1Rts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataBucket1Rts.setDescription('The count of the response times falling into bucket 1. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataBucket2Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket2Rts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataBucket2Rts.setDescription('The count of the response times falling into bucket 2. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataBucket3Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket3Rts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataBucket3Rts.setDescription('The count of the response times falling into bucket 3. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataBucket4Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket4Rts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataBucket4Rts.setDescription('The count of the response times falling into bucket 4. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataBucket5Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket5Rts.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataBucket5Rts.setDescription('The count of the response times falling into bucket 5. A management application can detect discontinuities in this counter by monitoring the tn3270eRtDataDiscontinuityTime object.')
tn3270eRtDataRtMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("responses", 1), ("timingMark", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataRtMethod.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataRtMethod.setDescription("The value of this object indicates the method that was used in calculating the IP network time. The value 'none(0) indicates that response times were not calculated for the IP network.")
tn3270eRtDataDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 20), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtDataDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which one or more of this entry's counter objects suffered a discontinuity. This may happen if a TN3270E server is stopped and then restarted, and local methods are used to set up collection policy (tn3270eRtCollCtlTable entries).")
tn3270eRtSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 34, 9, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tn3270eRtSpinLock.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtSpinLock.setDescription('An advisory lock used to allow cooperating TN3270E-RT-MIB applications to coordinate their use of the tn3270eRtCollCtlTable. When creating a new entry or altering an existing entry in the tn3270eRtCollCtlTable, an application should make use of tn3270eRtSpinLock to serialize application changes or additions. Since this is an advisory lock, the use of this lock is not enforced.')
tn3270eRtExceeded = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
if mibBuilder.loadTexts: tn3270eRtExceeded.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtExceeded.setDescription('This notification is generated when the average response time, tn3270eRtDataAvgRt, exceeds tn3270eRtCollCtlThresholdHigh at the end of a collection interval specified by tn3270eCollCtlSPeriod times tn3270eCollCtlSPMult. Note that the corresponding tn3270eCollCtlType must have traps(5) and average(3) set for this notification to be generated. In addition, tn3270eRtDataAvgCountTrans, tn3270eRtCollCtlThreshHigh, and tn3270eRtDataAvgRt are algorithmically compared to tn3270eRtCollCtlIdleCount for determination if this notification will be suppressed.')
tn3270eRtOkay = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 2)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
if mibBuilder.loadTexts: tn3270eRtOkay.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtOkay.setDescription('This notification is generated when the average response time, tn3270eRtDataAvgRt, falls below tn3270eRtCollCtlThresholdLow at the end of a collection interval specified by tn3270eCollCtlSPeriod times tn3270eCollCtlSPMult, after a tn3270eRtExceeded notification was generated. Note that the corresponding tn3270eCollCtlType must have traps(5) and average(3) set for this notification to be generated.')
tn3270eRtCollStart = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 3)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-MIB", "tn3270eResMapElementType"))
if mibBuilder.loadTexts: tn3270eRtCollStart.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollStart.setDescription('This notification is generated when response time data collection is enabled for a member of a client group. In order for this notification to occur the corresponding tn3270eRtCollCtlType must have traps(5) selected. tn3270eResMapElementType contains a valid value only if tn3270eRtDataClientAddress contains a valid address (rather than a zero-length octet string).')
tn3270eRtCollEnd = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 4)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
if mibBuilder.loadTexts: tn3270eRtCollEnd.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCollEnd.setDescription("This notification is generated when an tn3270eRtDataEntry is deleted after being active (actual data collected), in order to enable a management application monitoring an tn3270eRtDataEntry to get the entry's final values. Note that the corresponding tn3270eCollCtlType must have traps(5) set for this notification to be generated.")
tn3270eRtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 1))
tn3270eRtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 2))
tn3270eRtCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 9, 3, 2, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtGroup"), ("TN3270E-RT-MIB", "tn3270eRtNotGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn3270eRtCompliance = tn3270eRtCompliance.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtCompliance.setDescription('The compliance statement for agents that support the TN327E-RT-MIB.')
tn3270eRtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtCollCtlType"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPeriod"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPMult"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshHigh"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshLow"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlIdleCount"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry1"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry2"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry3"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry4"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlRowStatus"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtSpinLock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn3270eRtGroup = tn3270eRtGroup.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtGroup.setDescription('This group is mandatory for all implementations that support the TN3270E-RT-MIB. ')
tn3270eRtNotGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 2)).setObjects(("TN3270E-RT-MIB", "tn3270eRtExceeded"), ("TN3270E-RT-MIB", "tn3270eRtOkay"), ("TN3270E-RT-MIB", "tn3270eRtCollStart"), ("TN3270E-RT-MIB", "tn3270eRtCollEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn3270eRtNotGroup = tn3270eRtNotGroup.setStatus('current')
if mibBuilder.loadTexts: tn3270eRtNotGroup.setDescription('The notifications that must be supported when the TN3270E-RT-MIB is implemented. ')
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtDataTotalRts=tn3270eRtDataTotalRts, tn3270eRtDataAvgCountTrans=tn3270eRtDataAvgCountTrans, tn3270eRtDataClientAddress=tn3270eRtDataClientAddress, tn3270eRtCompliance=tn3270eRtCompliance, tn3270eRtCollCtlBucketBndry4=tn3270eRtCollCtlBucketBndry4, tn3270eRtCollCtlTable=tn3270eRtCollCtlTable, tn3270eRtCollCtlThreshHigh=tn3270eRtCollCtlThreshHigh, tn3270eRtCollCtlBucketBndry1=tn3270eRtCollCtlBucketBndry1, tn3270eRtDataTable=tn3270eRtDataTable, tn3270eRtCollCtlBucketBndry2=tn3270eRtCollCtlBucketBndry2, tn3270eRtDataAvgIpRt=tn3270eRtDataAvgIpRt, tn3270eRtDataBucket1Rts=tn3270eRtDataBucket1Rts, tn3270eRtDataBucket4Rts=tn3270eRtDataBucket4Rts, tn3270eRtDataDiscontinuityTime=tn3270eRtDataDiscontinuityTime, tn3270eRtCollCtlIdleCount=tn3270eRtCollCtlIdleCount, tn3270eRtSpinLock=tn3270eRtSpinLock, tn3270eRtCollCtlRowStatus=tn3270eRtCollCtlRowStatus, tn3270eRtDataIntTimeStamp=tn3270eRtDataIntTimeStamp, tn3270eRtCollCtlBucketBndry3=tn3270eRtCollCtlBucketBndry3, tn3270eRtExceeded=tn3270eRtExceeded, tn3270eRtCollCtlSPMult=tn3270eRtCollCtlSPMult, tn3270eRtDataBucket5Rts=tn3270eRtDataBucket5Rts, tn3270eRtOkay=tn3270eRtOkay, tn3270eRtCollStart=tn3270eRtCollStart, tn3270eRtGroups=tn3270eRtGroups, PYSNMP_MODULE_ID=tn3270eRtMIB, tn3270eRtCollCtlSPeriod=tn3270eRtCollCtlSPeriod, tn3270eRtDataRtMethod=tn3270eRtDataRtMethod, tn3270eRtDataBucket2Rts=tn3270eRtDataBucket2Rts, tn3270eRtObjects=tn3270eRtObjects, tn3270eRtCollEnd=tn3270eRtCollEnd, tn3270eRtDataCountTrans=tn3270eRtDataCountTrans, tn3270eRtDataElapsRndTrpSq=tn3270eRtDataElapsRndTrpSq, tn3270eRtDataBucket3Rts=tn3270eRtDataBucket3Rts, tn3270eRtNotGroup=tn3270eRtNotGroup, tn3270eRtMIB=tn3270eRtMIB, tn3270eRtCollCtlThreshLow=tn3270eRtCollCtlThreshLow, tn3270eRtDataCountDrs=tn3270eRtDataCountDrs, tn3270eRtCollCtlEntry=tn3270eRtCollCtlEntry, tn3270eRtGroup=tn3270eRtGroup, tn3270eRtDataAvgRt=tn3270eRtDataAvgRt, tn3270eRtDataTotalIpRts=tn3270eRtDataTotalIpRts, tn3270eRtCollCtlType=tn3270eRtCollCtlType, tn3270eRtDataEntry=tn3270eRtDataEntry, tn3270eRtDataElapsIpRtSq=tn3270eRtDataElapsIpRtSq, tn3270eRtDataClientPort=tn3270eRtDataClientPort, tn3270eRtCompliances=tn3270eRtCompliances, tn3270eRtNotifications=tn3270eRtNotifications, tn3270eRtDataClientAddrType=tn3270eRtDataClientAddrType, tn3270eRtConformance=tn3270eRtConformance)