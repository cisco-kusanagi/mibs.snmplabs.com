#
# PySNMP MIB module DL-SLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DL-SLA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Unsigned32, NotificationType, MibIdentifier, IpAddress, Integer32, NotificationType, Counter64, ModuleIdentity, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Unsigned32", "NotificationType", "MibIdentifier", "IpAddress", "Integer32", "NotificationType", "Counter64", "ModuleIdentity", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
digital_link = MibIdentifier((1, 3, 6, 1, 4, 1, 300)).setLabel("digital-link")
dl_ServiceLevelAgreement = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260)).setLabel("dl-ServiceLevelAgreement")
dlcSLAConfigurationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 1))
unitSLAConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 1, 1))
configSLA = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSLA.setStatus('mandatory')
if mibBuilder.loadTexts: configSLA.setDescription('This object represents whether SLA is enabled or disabled on this unit.')
unitSamplingPeriodForFDR_DDR = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setLabel("unitSamplingPeriodForFDR-DDR").setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSamplingPeriodForFDR_DDR.setStatus('mandatory')
if mibBuilder.loadTexts: unitSamplingPeriodForFDR_DDR.setDescription('This object is to configure the sampling period in minutes for Frame Delivery Ratio and Data Delivery Ratio. The default is 1 minute.')
unitSamplingPeriodForDelayMeasurement = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSamplingPeriodForDelayMeasurement.setStatus('mandatory')
if mibBuilder.loadTexts: unitSamplingPeriodForDelayMeasurement.setDescription('This object is to configure the sampling period in minutes for Delay Measurements. The default is 1 minute.')
unitThresholdForFDR = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitThresholdForFDR.setStatus('mandatory')
if mibBuilder.loadTexts: unitThresholdForFDR.setDescription('This object is to configure the threshold in one thousandth of a percentage for Frame Delivery Ratio. A value of 0 disables the trap altogether.')
unitThresholdForDDR = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitThresholdForDDR.setStatus('mandatory')
if mibBuilder.loadTexts: unitThresholdForDDR.setDescription('This object is to configure the threshold in one thousandth of a percentage for Data Delivery Ratio. A value of 0 disables the trap altogether.')
unitDelayMeasurementPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitDelayMeasurementPacketSize.setStatus('mandatory')
if mibBuilder.loadTexts: unitDelayMeasurementPacketSize.setDescription('This object is to configure the size in bytes of Delay Measurement Packets, one size of all DLCIs.')
unitOamDomainIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitOamDomainIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: unitOamDomainIdentifier.setDescription('This object is the Domain Identifier for OA&M protocol. All end points participating in this SLA measurement must have the SAME OA&M Domain Identifier. The default is 0.')
unitOamLocationIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitOamLocationIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: unitOamLocationIdentifier.setDescription('This object is the Location Identifier for OA&M protocol. All end points participating in this SLA measurement must have a unique OA&M Location Identifier.')
perDLCIConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 1, 2))
configurationPerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1), )
if mibBuilder.loadTexts: configurationPerDLCITable.setStatus('mandatory')
if mibBuilder.loadTexts: configurationPerDLCITable.setDescription('Configuration Table Per DLCI')
configurationPerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "configurationPerDLCITableIndex"))
if mibBuilder.loadTexts: configurationPerDLCIEntry.setStatus('mandatory')
if mibBuilder.loadTexts: configurationPerDLCIEntry.setDescription('An entry in the Configuration per DLCI table.')
configurationPerDLCITableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationPerDLCITableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: configurationPerDLCITableIndex.setDescription('The index of Configuration Per DLCI table, which is DLCI number.')
commitedInformationRatePerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commitedInformationRatePerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: commitedInformationRatePerDLCI.setDescription("This is the DLCI's Committed Information Rate (CIR). The CIR can be discovered automatically if LMI Rev 1.0 is used. If Annex A or Annex D is used, then the CIR must be entered manually in the DLCI table. The DLCI table is in the enterprise MIB.")
remoteDLCIPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteDLCIPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: remoteDLCIPerDLCI.setDescription('DLCI of the far end unit on each DLCI, which is discovered using Frame Relay OA&M Protocol. It will be stored in volatile memory.')
remoteIpAddressPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteIpAddressPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: remoteIpAddressPerDLCI.setDescription('IP Address of the NET port of the far end unit on each DLCI, which is discovered using Frame Relay OA&M Protocol. It will be stored in volatile memory.')
thresholdForDelayMeasurementsPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thresholdForDelayMeasurementsPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: thresholdForDelayMeasurementsPerDLCI.setDescription("This object represents this DLCI's delay threshold in milliseconds. The default is 64000. A value of 0 disables the trap altogether.")
dlcSLAStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2))
dlcDeliveryRatioStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2, 1))
deliveryRatioPerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1), )
if mibBuilder.loadTexts: deliveryRatioPerDLCITable.setStatus('mandatory')
if mibBuilder.loadTexts: deliveryRatioPerDLCITable.setDescription('Lifetime Delivery counter Table Per DLCI, contains both Frame Delivery Ratio and Data Delivery Ratio.')
deliveryRatioPerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"))
if mibBuilder.loadTexts: deliveryRatioPerDLCIEntry.setStatus('mandatory')
if mibBuilder.loadTexts: deliveryRatioPerDLCIEntry.setDescription('An entry in the Delivery Ratio table.')
deliveryRatioPerDLCITableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deliveryRatioPerDLCITableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: deliveryRatioPerDLCITableIndex.setDescription('The index of Delivery Ratio Table, which is the same value as configurationPerDLCITableIndex.')
deliveryTableEncodedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deliveryTableEncodedValue.setStatus('mandatory')
if mibBuilder.loadTexts: deliveryTableEncodedValue.setDescription("This object represents the value of the whole row of the table. If the table. The intent of object is to increase the efficiency of retrieving the table. For each object value in this table, which are all of Counter type, it will be represented with 4 bytes of data. The byte order of the Counter value will be MSB ... LSB. This object will contain the value of all objects on the table, except 'deliveryRatioPerDLCITableIndex'.")
deliveryTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deliveryTableTimestamp.setStatus('obsolete')
if mibBuilder.loadTexts: deliveryTableTimestamp.setDescription("Timestamp of the last sample for delivery Entry statistics. Each time the near end of the DLCI receives Delivery Ratio Results Information Field, this number will contain the unit's current timestamp. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.")
fTCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTCLperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fTCLperDLCI.setDescription('Number of frames transmitted at the near end within CIR on this DLCI.')
fTELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTELperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fTELperDLCI.setDescription('Number of frames transmitted at the near end above CIR on this DLCI')
fRCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRCLperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fRCLperDLCI.setDescription('Number of frames received at the near end on this DLCI within CIR. These frames will have the Discard Eligible (DE) bit reset.')
fRELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRELperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fRELperDLCI.setDescription('Number of frames received at the near end on this DLCI above CIR. These frames will have the Discard Eligible (DE) bit set.')
fTCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTCRperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fTCRperDLCI.setDescription('Number of frames transmitted at the far end within CIR on this DLCI.')
fTERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTERperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fTERperDLCI.setDescription('Number of frames transmitted at the far end above CIR on this DLCI.')
fRCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRCRperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fRCRperDLCI.setDescription('Number of frames received at the far end on this DLCI within CIR. These frames will have the Discard Eligible (DE) bit reset.')
fRERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRERperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: fRERperDLCI.setDescription('Number of frames received at the far end on this DLCI above CIR. These frames will have the Discard Eligible (DE) bit set.')
fDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fDRNumberOfSamplesTaken.setStatus('obsolete')
if mibBuilder.loadTexts: fDRNumberOfSamplesTaken.setDescription('Number of samples taken for Frame Delivery Statistics. Each time the near end receives the Frame Delivery Ratio Results Information Field, this counter will be incremented.')
fDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fDRNumberOfThresholdViolations.setStatus('obsolete')
if mibBuilder.loadTexts: fDRNumberOfThresholdViolations.setDescription("Number of threshold violations for Frame Delivery. FDRCL = fRCRPerDLCI / fTCLPerDLCI FDRCR = fRCLPerDLCI / fTCRPerDLCI For each sample, FDRCL and FDRCR are compared to the threshold configured on object 'unitThresholdForFDR'. When either FDRCL or FDRCR is less than the threshold, this counter is incremented.")
dTCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTCLperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dTCLperDLCI.setDescription('Number of bytes transmitted to the network within CIR on this DLCI.')
dTELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTELperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dTELperDLCI.setDescription('Number of bytes transmitted to the network above CIR on this DLCI')
dRCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRCLperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dRCLperDLCI.setDescription('Number of bytes received at the near end on this DLCI within CIR. These frames will have the Discard Eligible (DE) bit reset.')
dRELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRELperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dRELperDLCI.setDescription('Number of bytes received at the near end of this DLCI above CIR. These frames will have the Discard Eligible (DE) bit set.')
dTCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTCRperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dTCRperDLCI.setDescription('Number of bytes transmitted at the far end within CIR on this DLCI.')
dTERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTERperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dTERperDLCI.setDescription('Number of bytes transmitted at the far end above CIR on this DLCI.')
dRCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRCRperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dRCRperDLCI.setDescription('Number of bytes received at the far end on this DLCI above CIR. These frames will have the Discard Eligible (DE) bit reset.')
dRERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRERperDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: dRERperDLCI.setDescription('Number of bytes received at the far end on his DLCI above CIR. These frames will have the Discard Eligible (DE) bit set.')
dDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dDRNumberOfSamplesTaken.setStatus('obsolete')
if mibBuilder.loadTexts: dDRNumberOfSamplesTaken.setDescription('Number of samples taken for Data Delivery statistics. Each time the near end receives the Data Delivery Ratio Results Information Field, this counter will be incremented.')
dDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dDRNumberOfThresholdViolations.setStatus('obsolete')
if mibBuilder.loadTexts: dDRNumberOfThresholdViolations.setDescription("Number of threshold violations for Data Delivery statistics. DDRCL = dRCRPerDLCI / dTCLPerDLCI DDRCR = dRCLPerDLCI / dTCRPerDLCI For each sample, DDRCL and DDRCR are compared to the threshold configured on object 'unitThresholdForDDR'. When either DDRCL or DDRCR is less than the threshold, this counter is incremented.")
txFDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFDRTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: txFDRTimestamp.setDescription("Timestamp of the last sample for delivery Entry statistics. Each time the near end of the DLCI receives Delivery Ratio Results Information Field, this number will contain the unit's current timestamp. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.")
txFDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFDRNumberOfSamplesTaken.setStatus('mandatory')
if mibBuilder.loadTexts: txFDRNumberOfSamplesTaken.setDescription('Number of samples taken for Frame Delivery Statistics. Each time the near end receives the Frame Delivery Ratio Results Information Field, this counter will be incremented.')
txFDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFDRNumberOfThresholdViolations.setStatus('mandatory')
if mibBuilder.loadTexts: txFDRNumberOfThresholdViolations.setDescription("Number of threshold violations for Frame Delivery. FDRCL = fRCRPerDLCI / fTCLPerDLCI For each sample, FDRCL is compared to the threshold configured on object 'unitThresholdForFDR'. When FDRCL is less than the threshold, this counter is incremented.")
rxFDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFDRTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: rxFDRTimestamp.setDescription("Timestamp of the last sample for delivery Entry statistics. Each time the near end of the DLCI receives Delivery Ratio poll, this number will contain the unit's current timestamp. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.")
rxFDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFDRNumberOfSamplesTaken.setStatus('mandatory')
if mibBuilder.loadTexts: rxFDRNumberOfSamplesTaken.setDescription('Number of samples taken for Frame Delivery Statistics. Each time the near end receives the Frame Delivery Ratio poll, this counter will be incremented.')
rxFDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFDRNumberOfThresholdViolations.setStatus('mandatory')
if mibBuilder.loadTexts: rxFDRNumberOfThresholdViolations.setDescription("Number of threshold violations for Frame Delivery. FDRCR = fRCLPerDLCI / fTCRPerDLCI For each sample, FDRCR is compared to the threshold configured on object 'unitThresholdForFDR'. When FDRCR is less than the threshold, this counter is incremented.")
txDDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDDRTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: txDDRTimestamp.setDescription("Timestamp of the last sample for delivery Entry statistics. Each time the near end of the DLCI receives Delivery Ratio Results Information Field, this number will contain the unit's current timestamp. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.")
txDDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDDRNumberOfSamplesTaken.setStatus('mandatory')
if mibBuilder.loadTexts: txDDRNumberOfSamplesTaken.setDescription('Number of samples taken for DataDelivery Statistics. Each time the near end receives the Data Delivery Ratio Results Information Field, this counter will be incremented.')
txDDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDDRNumberOfThresholdViolations.setStatus('mandatory')
if mibBuilder.loadTexts: txDDRNumberOfThresholdViolations.setDescription("Number of threshold violations for Data Delivery. DDRCL = dRCRPerDLCI / dTCLPerDLCI For each sample, DDRCL is compared to the threshold configured on object 'unitThresholdForDDR'. When DDRCL is less than the threshold, this counter is incremented.")
rxDDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDDRTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: rxDDRTimestamp.setDescription("Timestamp of the last sample for delivery Entry statistics. Each time the near end of the DLCI receives Delivery Ratio poll, this number will contain the unit's current timestamp. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.")
rxDDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDDRNumberOfSamplesTaken.setStatus('mandatory')
if mibBuilder.loadTexts: rxDDRNumberOfSamplesTaken.setDescription('Number of samples taken for Data Delivery Statistics. Each time the near end receives the Data Delivery Ratio poll, this counter will be incremented.')
rxDDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDDRNumberOfThresholdViolations.setStatus('mandatory')
if mibBuilder.loadTexts: rxDDRNumberOfThresholdViolations.setDescription("Number of threshold violations for Data Delivery. DDRCR = dRCLPerDLCI / dTCRPerDLCI For each sample, DDRCR is compared to the threshold configured on object 'unitThresholdForDDR'. When DDRCR is less than the threshold, this counter is incremented.")
txDiscardEligible = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDiscardEligible.setStatus('mandatory')
if mibBuilder.loadTexts: txDiscardEligible.setDescription("Number of Discard Eligible counters transmitted at the near end. This counter has the same value as object 'etherStatsFragments' in RMON MIB (RFC 1757) for DTE port.")
rxDiscardEligible = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDiscardEligible.setStatus('mandatory')
if mibBuilder.loadTexts: rxDiscardEligible.setDescription("Number of Discard Eligible counters received by the near end. This counter has the same value as object 'etherStatsFragments' in RMON MIB (RFC 1757) for DCE port")
txFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFECN.setStatus('mandatory')
if mibBuilder.loadTexts: txFECN.setDescription("Number of FECN counters transmitted at the near end. This counter has the same value as object 'etherStatsCollisions' in RMON MIB (RFC 1757) for DTE port.")
rxFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFECN.setStatus('mandatory')
if mibBuilder.loadTexts: rxFECN.setDescription("Number of FECN counters received by the near end. This counter has the same value as object 'etherStatsCollisions' in RMON MIB (RFC 1757) for DCE port.")
txBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txBECN.setStatus('mandatory')
if mibBuilder.loadTexts: txBECN.setDescription("Number of BECN counters transmitted at the near end. This counter has the same value as object 'etherStatsJabbers' in RMON MIB (RFC 1757) for DTE port.")
rxBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxBECN.setStatus('mandatory')
if mibBuilder.loadTexts: rxBECN.setDescription("Number of BECN counters received by the near end. This counter has the same value as object 'etherStatsJabbers' in RMON MIB (RFC 1757) for DCE port.")
dlcDelayStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2, 2))
delayPerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1), )
if mibBuilder.loadTexts: delayPerDLCITable.setStatus('mandatory')
if mibBuilder.loadTexts: delayPerDLCITable.setDescription('Delay Table Per DLCI')
delayPerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "delayPerDLCITableIndex"))
if mibBuilder.loadTexts: delayPerDLCIEntry.setStatus('mandatory')
if mibBuilder.loadTexts: delayPerDLCIEntry.setDescription('An entry in the Delay per DLCI table.')
delayPerDLCITableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayPerDLCITableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: delayPerDLCITableIndex.setDescription('The index of Delay Table, which is DLCI number.')
delayTableEncodedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayTableEncodedValue.setStatus('mandatory')
if mibBuilder.loadTexts: delayTableEncodedValue.setDescription("This object represents the value of the whole row of the table. If the table. The intent of object is to increase the efficiency of retrieving the table. For each object value in this table, which are all of Counter type, it will be represented with 4 bytes of data. The byte order of the Counter value will be MSB ... LSB. This object will contain the value of all objects on the table, except 'delayPerDLCITableIndex'.")
delayTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayTableTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: delayTableTimestamp.setDescription("Timestamp for Delay Table entry. Each time the near end of the DLCI receives an OA&M message containing a Frame Transfer Delay Information Field, this number will contain the unit's current timestamp. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.")
totalRoundTripDelayPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalRoundTripDelayPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: totalRoundTripDelayPerDLCI.setDescription('Sum of all the round trip delay measurements taken so far.')
maximumRoundTripDelayNSamplesPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumRoundTripDelayNSamplesPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: maximumRoundTripDelayNSamplesPerDLCI.setDescription('Maximum Round Trip Delay in last n samples. N is 15.')
maximumRoundTripDelay2NSamplesPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumRoundTripDelay2NSamplesPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: maximumRoundTripDelay2NSamplesPerDLCI.setDescription('Maximum Round Trip Delay in last 2N samples. N is 15.')
maximumRoundTripDelay4NSamplesPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumRoundTripDelay4NSamplesPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: maximumRoundTripDelay4NSamplesPerDLCI.setDescription('Maximum Round Trip Delay in last 4n samples. N is 15.')
numberOfDelayMeasurementsPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfDelayMeasurementsPerDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: numberOfDelayMeasurementsPerDLCI.setDescription('Number of delay measurements per DLCI. Each time the near end receives an OA&M message containing a Frame Transfer Delay Information Field, this counter will be incremented.')
delayNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayNumberOfThresholdViolations.setStatus('mandatory')
if mibBuilder.loadTexts: delayNumberOfThresholdViolations.setDescription("Number of threshold violations on Delay measurement. If an individual delay measurement on this DLCI is greater than the threshold value configured in object 'thresholdForDelayMeasurementPerDLCI', this counter will be incremented.")
dlcOutageStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2, 3))
outagePerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1), )
if mibBuilder.loadTexts: outagePerDLCITable.setStatus('mandatory')
if mibBuilder.loadTexts: outagePerDLCITable.setDescription('Outage Table Per DLCI')
outagePerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "outageTableIndex"))
if mibBuilder.loadTexts: outagePerDLCIEntry.setStatus('mandatory')
if mibBuilder.loadTexts: outagePerDLCIEntry.setDescription('An entry in the Outage per DLCI table.')
outageTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: outageTableIndex.setDescription('Index of Outage Table, which is the DLCI number.')
outageTableEncodedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableEncodedValue.setStatus('mandatory')
if mibBuilder.loadTexts: outageTableEncodedValue.setDescription("This object represents the value of the whole row of the table. If the table. The intent of object is to increase the efficiency of retrieving the table. For each object value in this table, which are all of Counter type, it will be represented with 4 bytes of data. The byte order of the Counter value will be MSB ... LSB. This object will contain the value of all objects on the table, except 'outageTableIndex'.")
outageTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: outageTableTimestamp.setDescription('Timestamp of when this Outage Table entry last updated. A timestamp is a 32-bit number representing the number of seconds that have elapsed since 12:00AM, January 1, 1970.')
outageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("no-outage", 2), ("excluded-outage", 3), ("included-outage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageStatus.setStatus('mandatory')
if mibBuilder.loadTexts: outageStatus.setDescription('')
numberOfOutageCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfOutageCounter.setStatus('mandatory')
if mibBuilder.loadTexts: numberOfOutageCounter.setDescription('Number of outages.')
periodOfOutages = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: periodOfOutages.setStatus('mandatory')
if mibBuilder.loadTexts: periodOfOutages.setDescription('The sum total of how long the outages are.')
numberOfExcludedOutageCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfExcludedOutageCounter.setStatus('mandatory')
if mibBuilder.loadTexts: numberOfExcludedOutageCounter.setDescription('Number of excluded outages.')
periodOfExcludedOutages = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: periodOfExcludedOutages.setStatus('mandatory')
if mibBuilder.loadTexts: periodOfExcludedOutages.setDescription('The sum total of how long excluded outages are.')
outageTableLastTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableLastTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: outageTableLastTimestamp.setDescription("This object contains timestamp (in seconds) of the last time 'outagePerDLCITable' is updated (changed).")
fDRThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 300, 260) + (0,1)).setObjects(("DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"))
if mibBuilder.loadTexts: fDRThresholdTrap.setDescription("This trap will be sent if 'fDRNumberOfThresholdViolations' is incremented. The VARIABLES contain the DLCI number whose Frame Delivery Ratio threshold violation is updated.")
dDRThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 300, 260) + (0,2)).setObjects(("DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"))
if mibBuilder.loadTexts: dDRThresholdTrap.setDescription("This trap will be sent if 'dDRNumberOfThresholdViolations' is incremented. The VARIABLES contain the DLCI number whose Data Delivery Ratio threshold violation is updated.")
delayThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 300, 260) + (0,3)).setObjects(("DL-SLA-MIB", "delayPerDLCITableIndex"))
if mibBuilder.loadTexts: delayThresholdTrap.setDescription("This trap will be sent if 'delayNumberOfThresholdViolations' is incremented. The VARIABLES contain the DLCI number whose Delay threshold violation is updated.")
mibBuilder.exportSymbols("DL-SLA-MIB", delayNumberOfThresholdViolations=delayNumberOfThresholdViolations, unitOamDomainIdentifier=unitOamDomainIdentifier, configurationPerDLCITableIndex=configurationPerDLCITableIndex, perDLCIConfiguration=perDLCIConfiguration, delayThresholdTrap=delayThresholdTrap, dTERperDLCI=dTERperDLCI, thresholdForDelayMeasurementsPerDLCI=thresholdForDelayMeasurementsPerDLCI, dDRNumberOfSamplesTaken=dDRNumberOfSamplesTaken, rxFDRNumberOfThresholdViolations=rxFDRNumberOfThresholdViolations, dRCRperDLCI=dRCRperDLCI, dlcOutageStatistics=dlcOutageStatistics, unitSamplingPeriodForFDR_DDR=unitSamplingPeriodForFDR_DDR, delayPerDLCITable=delayPerDLCITable, deliveryRatioPerDLCITableIndex=deliveryRatioPerDLCITableIndex, numberOfExcludedOutageCounter=numberOfExcludedOutageCounter, delayTableEncodedValue=delayTableEncodedValue, fDRNumberOfThresholdViolations=fDRNumberOfThresholdViolations, outageTableEncodedValue=outageTableEncodedValue, outagePerDLCITable=outagePerDLCITable, dRERperDLCI=dRERperDLCI, dRCLperDLCI=dRCLperDLCI, numberOfOutageCounter=numberOfOutageCounter, deliveryRatioPerDLCIEntry=deliveryRatioPerDLCIEntry, txDDRTimestamp=txDDRTimestamp, unitThresholdForDDR=unitThresholdForDDR, rxDDRTimestamp=rxDDRTimestamp, fRCRperDLCI=fRCRperDLCI, fRERperDLCI=fRERperDLCI, dRELperDLCI=dRELperDLCI, maximumRoundTripDelay4NSamplesPerDLCI=maximumRoundTripDelay4NSamplesPerDLCI, remoteIpAddressPerDLCI=remoteIpAddressPerDLCI, dTCLperDLCI=dTCLperDLCI, txFDRTimestamp=txFDRTimestamp, delayTableTimestamp=delayTableTimestamp, outageStatus=outageStatus, fRELperDLCI=fRELperDLCI, configurationPerDLCIEntry=configurationPerDLCIEntry, numberOfDelayMeasurementsPerDLCI=numberOfDelayMeasurementsPerDLCI, periodOfExcludedOutages=periodOfExcludedOutages, dTELperDLCI=dTELperDLCI, configSLA=configSLA, remoteDLCIPerDLCI=remoteDLCIPerDLCI, txFDRNumberOfThresholdViolations=txFDRNumberOfThresholdViolations, deliveryTableEncodedValue=deliveryTableEncodedValue, fTCRperDLCI=fTCRperDLCI, totalRoundTripDelayPerDLCI=totalRoundTripDelayPerDLCI, outageTableTimestamp=outageTableTimestamp, fRCLperDLCI=fRCLperDLCI, txDiscardEligible=txDiscardEligible, maximumRoundTripDelay2NSamplesPerDLCI=maximumRoundTripDelay2NSamplesPerDLCI, deliveryRatioPerDLCITable=deliveryRatioPerDLCITable, unitSamplingPeriodForDelayMeasurement=unitSamplingPeriodForDelayMeasurement, fDRThresholdTrap=fDRThresholdTrap, delayPerDLCITableIndex=delayPerDLCITableIndex, delayPerDLCIEntry=delayPerDLCIEntry, rxDiscardEligible=rxDiscardEligible, digital_link=digital_link, dlcDeliveryRatioStatistics=dlcDeliveryRatioStatistics, txFDRNumberOfSamplesTaken=txFDRNumberOfSamplesTaken, dlcSLAConfigurationGroup=dlcSLAConfigurationGroup, configurationPerDLCITable=configurationPerDLCITable, txDDRNumberOfSamplesTaken=txDDRNumberOfSamplesTaken, dDRThresholdTrap=dDRThresholdTrap, commitedInformationRatePerDLCI=commitedInformationRatePerDLCI, unitOamLocationIdentifier=unitOamLocationIdentifier, txFECN=txFECN, rxDDRNumberOfThresholdViolations=rxDDRNumberOfThresholdViolations, outageTableIndex=outageTableIndex, rxDDRNumberOfSamplesTaken=rxDDRNumberOfSamplesTaken, dlcDelayStatistics=dlcDelayStatistics, txDDRNumberOfThresholdViolations=txDDRNumberOfThresholdViolations, periodOfOutages=periodOfOutages, rxFECN=rxFECN, dlcSLAStatisticsGroup=dlcSLAStatisticsGroup, txBECN=txBECN, dl_ServiceLevelAgreement=dl_ServiceLevelAgreement, maximumRoundTripDelayNSamplesPerDLCI=maximumRoundTripDelayNSamplesPerDLCI, rxFDRTimestamp=rxFDRTimestamp, outageTableLastTimestamp=outageTableLastTimestamp, unitDelayMeasurementPacketSize=unitDelayMeasurementPacketSize, unitSLAConfiguration=unitSLAConfiguration, deliveryTableTimestamp=deliveryTableTimestamp, fTCLperDLCI=fTCLperDLCI, dTCRperDLCI=dTCRperDLCI, unitThresholdForFDR=unitThresholdForFDR, dDRNumberOfThresholdViolations=dDRNumberOfThresholdViolations, rxBECN=rxBECN, fDRNumberOfSamplesTaken=fDRNumberOfSamplesTaken, fTERperDLCI=fTERperDLCI, rxFDRNumberOfSamplesTaken=rxFDRNumberOfSamplesTaken, outagePerDLCIEntry=outagePerDLCIEntry, fTELperDLCI=fTELperDLCI)
