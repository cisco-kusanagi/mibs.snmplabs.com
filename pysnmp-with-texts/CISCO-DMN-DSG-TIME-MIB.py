#
# PySNMP MIB module CISCO-DMN-DSG-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-TIME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Integer32, ModuleIdentity, Bits, Counter64, Counter32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "Bits", "Counter64", "Counter32", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGTime = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23))
ciscoDSGTime.setRevisions(('2010-08-30 11:00', '2010-04-12 06:00', '2009-12-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGTime.setRevisionsDescriptions(('V01.00.02 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.01 2010-04-12 The description of timeCurrent is updated.', 'V01.00.00 2009-12-20 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGTime.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGTime.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGTime.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGTime.setDescription('Cisco Time Information MIB.')
timeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1))
timeFormat = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("twentyFourHr", 1), ("twentyFourHrSuspendZero", 2), ("twelveHr", 3), ("twelveHrSuspendZero", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeFormat.setStatus('current')
if mibBuilder.loadTexts: timeFormat.setDescription('Time format to be used to display the time.')
timeDateFormat = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("yyyymmdd", 1), ("ddmmyyyy", 2), ("mmddyyyy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateFormat.setStatus('current')
if mibBuilder.loadTexts: timeDateFormat.setDescription('Date format to be used to display the date.')
timeGMTOffset = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33))).clone(namedValues=NamedValues(("minusTwelve", 1), ("minusEleven", 2), ("minusTen", 3), ("minusNine", 4), ("minusEight", 5), ("minusSeven", 6), ("minusSix", 7), ("minusFive", 8), ("minusFour", 9), ("minusThreeAndAHalf", 10), ("minusTwo", 12), ("minusOne", 13), ("zeroGMT", 14), ("plusOne", 15), ("plusTwo", 16), ("plusThree", 17), ("plusThreeAndAHalf", 18), ("plusFour", 19), ("plusFourAndAHalf", 20), ("plusFive", 21), ("plusFiveAndAHalf", 22), ("plusFiveAndThreeQuarter", 23), ("plusSix", 24), ("plusSixAndAHalf", 25), ("plusSeven", 26), ("plusEight", 27), ("plusNine", 28), ("plusNineAndAHalf", 29), ("plusTen", 30), ("plusEleven", 31), ("plusTwelve", 32), ("plusThirteen", 33)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeGMTOffset.setStatus('current')
if mibBuilder.loadTexts: timeGMTOffset.setDescription('Local Time Offset. -12 to +13 hours ( 01 ) - 12.0, ( 02 ) - 11.0 ( 03 ) - 10.0, ( 04 ) - 9.0 ( 05 ) - 8.0, ( 06 ) - 7.0 ( 07 ) - 6.0, ( 08 ) - 5.0 ( 09 ) - 4.0, ( 10 ) - 3.5 ( 12 ) - 2.0, ( 13 ) - 1.0 ( 14 ) - 0.0, ( 15 ) + 1.0 ( 16 ) + 2.0, ( 17 ) + 3.0 ( 18 ) + 3.5, ( 19 ) + 4.0 ( 20 ) + 4.5, ( 21 ) + 5.0 ( 22 ) + 5.5, ( 23 ) + 5.75 ( 24 ) + 6.0, ( 25 ) + 6.5 ( 26 ) + 7.0, ( 27 ) + 8.0 ( 28 ) + 9.0, ( 29 ) + 9.5 ( 30 ) + 10.0, ( 31 ) + 11.0 ( 32 ) + 12.0, ( 33 ) + 13.0')
timeCurrent = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeCurrent.setStatus('current')
if mibBuilder.loadTexts: timeCurrent.setDescription('It displays the current date and time taking into account the value of timeGMTOffset, as per the format specified by timeDateFormat and timeFormat.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-TIME-MIB", PYSNMP_MODULE_ID=ciscoDSGTime, timeDateFormat=timeDateFormat, timeCurrent=timeCurrent, timeFormat=timeFormat, timeInfo=timeInfo, timeGMTOffset=timeGMTOffset, ciscoDSGTime=ciscoDSGTime)
