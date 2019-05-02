#
# PySNMP MIB module ATT-CNM-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATT-CNM-DS3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, enterprises, Counter64, iso, Unsigned32, Integer32, NotificationType, ObjectIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "enterprises", "Counter64", "iso", "Unsigned32", "Integer32", "NotificationType", "ObjectIdentity", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
att_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 74)).setLabel("att-2")
att_products = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1)).setLabel("att-products")
att_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2)).setLabel("att-mgmt")
att_cnmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1, 9)).setLabel("att-cnmAgent")
att_cnm = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15)).setLabel("att-cnm")
att_cnm_ds3 = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15, 4)).setLabel("att-cnm-ds3")
attCNMds3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1), )
if mibBuilder.loadTexts: attCNMds3ConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ConfigTable.setDescription('A list of entries containing configuration information for all DS3 interfaces managed by this system.')
attCNMds3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1), ).setIndexNames((0, "ATT-CNM-DS3-MIB", "attCNMds3ConfigIndex"))
if mibBuilder.loadTexts: attCNMds3ConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ConfigEntry.setDescription('An entry containing configuration information for a particular DS3 interface.')
attCNMds3ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ConfigIndex.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ConfigIndex.setDescription('A unique value for each DS3 interface. The interface identified by a particular value of this index is the same interface as identified by the same value of an attCNMifConfigIndex object instance.')
attCNMds3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("ds3M23", 2), ("ds3SYNTRAN", 3), ("ds3CbitParity", 4), ("ds3ClearChannel", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LineType.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3LineType.setDescription('This variable indicates the variety of DS3 C-bit application supported by this interface. For SMDS, this variable will have the value ds3ClearChannel, denoting that this interface supports the clear-channel with C-bit usage unspecified as specified by ANSI.')
attCNMds3ZeroCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3other", 1), ("ds3B3ZS", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ZeroCoding.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ZeroCoding.setDescription('This variable describes the variety of zero code suppression/substitution used on the DS3 interface its characteristics.')
attCNMds3ErrorsMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsMaxIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsMaxIntervals.setDescription('This variable identifies the maximum number of measurement intervals supported for the error counts maintained by this DS3 interface in the attCNMds3ErrorsTable.')
attCNMds3ErrorsIntervalLen = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsIntervalLen.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsIntervalLen.setDescription('This variable identifies the number of seconds that make up one complete measurement interval for the error counts maintained by this DS3 interface in the attCNMds3ErrorsTable.')
attCNMds3StatusTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2), )
if mibBuilder.loadTexts: attCNMds3StatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3StatusTable.setDescription('A list of entries containing status information for all DS3 interfaces managed by this system.')
attCNMds3StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1), ).setIndexNames((0, "ATT-CNM-DS3-MIB", "attCNMds3StatusIndex"))
if mibBuilder.loadTexts: attCNMds3StatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3StatusEntry.setDescription('An entry containing status information for a particular DS3 interface.')
attCNMds3StatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3StatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3StatusIndex.setDescription('A unique value for each DS3 interface. The interface identified by a particular value of this index is the same interface as identified by the same value of an attCNMifConfigIndex object instance.')
attCNMds3LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LineStatus.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3LineStatus.setDescription('This variable indicates the most Line Status of this interface. This object is a bit map represented as a sum, therefore, it can represent multiple failures (alarms) simultaneously. The various bit positions are: 1 No Alarm Present 2 Yellow Alarm 4 Near End Alarm-Indication-Signal 8 Near End Loss-Of-Frame 16 Near End Loss-Of-Signal For example, for an interface that has LOF and LOS outstanding, this object will have a value of 24.')
attCNMds3ErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3), )
if mibBuilder.loadTexts: attCNMds3ErrorsTable.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsTable.setDescription('A list of entries containing protocol error counts, maintained during the specified measurement interval, for all DS3 interfaces managed by this system.')
attCNMds3ErrorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1), ).setIndexNames((0, "ATT-CNM-DS3-MIB", "attCNMds3ErrorsIndex"), (0, "ATT-CNM-DS3-MIB", "attCNMds3ErrorsInterval"))
if mibBuilder.loadTexts: attCNMds3ErrorsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsEntry.setDescription('An entry containing protocol error counts, maintained during the specified measurement interval, for a particular DS3 interface.')
attCNMds3ErrorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsIndex.setDescription('A unique value for each DS3 interface. The interface identified by a particular value of this index is the same interface as identified by the same value of an attCNMifConfigIndex object instance.')
attCNMds3ErrorsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsInterval.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsInterval.setDescription('This variable identifies the measurement interval number for which measurement is provided. It is a number between 1 and XX, where 1 identifies the most recently completed measurement interval and XX is the least recently completed measurement interval. The value of XX is specified by the attCNMds3ErrorsMaxIntervals object given in the attCNMds3ConfigTable. The maximum length of each measurement interval is specified by the attCNMds3ErrorsIntervalLen object given in the attCNMds3ConfigTable.')
attCNMds3ErrorsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsTimeStamp.setDescription('The time stamp corresponding to the end of the specified measurement interval, as measured in seconds from 00:00:00 UTC (Coordinated Universal Time) January 1, 1970. Any fraction is rounded up.')
attCNMds3ErrorsLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsLocalTime.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ErrorsLocalTime.setDescription('The time stamp corresponding to the end of the specified measurement interval. Any fraction is rounded up. It is given as a printable ASCII string showing the local time at the end of the interval.')
attCNMds3LCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LCVs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3LCVs.setDescription('The counter associated with the number of Line Code Violations encountered by a DS3 interface during the specified measurement interval. For a B3ZS-coded signal, a Line Code Violation is the occurrence of a received bipolar violation that is not part of a zero-substitution code. For a B3ZS signal, an LCV may also include other error patterns such as: three consecutive zeros and incorrect parity. The Bipolar Violation Rate is generally viewed as approximating the Bit Error Rate.')
attCNMds3LESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LESs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3LESs.setDescription('The counter associated with the number of Line Errored Seconds encountered by a DS3 interface during the specified measurement interval. A Line Errored Second is any second with at least one Line Code Violation.')
attCNMds3LSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LSESs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3LSESs.setDescription('The counter associated with the number of Line Severely Errored Seconds encountered by a DS3 interface during the specified measurement interval. A Line Severely Errored Second is any second with 45 or more Line Code Violations monitored at the DS3 rate.')
attCNMds3CVs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3CVs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3CVs.setDescription('The counter associated with the number of Code Violations encountered by a DS3 interface during the specified measurement interval. For SMDS, a DS3 Code Violation is an occurrence of a P-bit error. Excessive Coding Violations signifies a faulty transmission line.')
attCNMds3ESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ESs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3ESs.setDescription('The counter associated with the number of Errored Seconds encountered by a DS3 interface during the specified measurement interval. For SMDS DS3 signals, this is the number of seconds during which at least one error occurred which is a P-bit error or a Severely Errored Framing event.')
attCNMds3SESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3SESs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3SESs.setDescription('The counter associated with the number of Severely Errored Seconds encountered by a DS3 interface during the specified measurement interval. For SMDS DS3 signals, this is the number of seconds during which 44 or more P-bit errors occurred or at least one Severely Errored Framing event occurred. All Severely Errored Seconds are also counted as Errored Seconds.')
attCNMds3SEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3SEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3SEFSs.setDescription('The counter associated with the number of Severely Errored Framing Seconds encountered by a DS3 interface during the specified measurement interval. A Severely Errored Framing Second is any second during which one or more Severely Errored Framing (SEF) events occurred. A Severely Errored Framing event is declared when 3 or more errors in 16 or fewer consecutive F-bits occur within a DS3 M-frame.')
attCNMds3UASs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3UASs.setStatus('mandatory')
if mibBuilder.loadTexts: attCNMds3UASs.setDescription('The counter associated with the number of Unavailable Seconds encountered by a DS3 interface during the specified measurement interval. An Unavailable Second is any second during which the DS3 interface was unavailable to offer service.')
mibBuilder.exportSymbols("ATT-CNM-DS3-MIB", att_cnm_ds3=att_cnm_ds3, attCNMds3ConfigIndex=attCNMds3ConfigIndex, attCNMds3LineType=attCNMds3LineType, attCNMds3StatusTable=attCNMds3StatusTable, attCNMds3LineStatus=attCNMds3LineStatus, attCNMds3ESs=attCNMds3ESs, attCNMds3UASs=attCNMds3UASs, attCNMds3ErrorsTable=attCNMds3ErrorsTable, attCNMds3LESs=attCNMds3LESs, att_cnmAgent=att_cnmAgent, att_2=att_2, attCNMds3CVs=attCNMds3CVs, attCNMds3SEFSs=attCNMds3SEFSs, attCNMds3ErrorsMaxIntervals=attCNMds3ErrorsMaxIntervals, attCNMds3ErrorsIndex=attCNMds3ErrorsIndex, attCNMds3ErrorsLocalTime=attCNMds3ErrorsLocalTime, attCNMds3LSESs=attCNMds3LSESs, attCNMds3StatusIndex=attCNMds3StatusIndex, attCNMds3ErrorsEntry=attCNMds3ErrorsEntry, att_mgmt=att_mgmt, attCNMds3ErrorsIntervalLen=attCNMds3ErrorsIntervalLen, attCNMds3ConfigTable=attCNMds3ConfigTable, attCNMds3SESs=attCNMds3SESs, att_products=att_products, attCNMds3ZeroCoding=attCNMds3ZeroCoding, att_cnm=att_cnm, attCNMds3LCVs=attCNMds3LCVs, attCNMds3StatusEntry=attCNMds3StatusEntry, attCNMds3ConfigEntry=attCNMds3ConfigEntry, attCNMds3ErrorsInterval=attCNMds3ErrorsInterval, attCNMds3ErrorsTimeStamp=attCNMds3ErrorsTimeStamp)
