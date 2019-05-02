#
# PySNMP MIB module NETASQ-PROPERTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETASQ-PROPERTY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ntqProductProperty, = mibBuilder.importSymbols("NETASQ-SMI-MIB", "ntqProductProperty")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, TimeTicks, Gauge32, MibIdentifier, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter32, ObjectIdentity, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "TimeTicks", "Gauge32", "MibIdentifier", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntqModel = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqModel.setStatus('current')
if mibBuilder.loadTexts: ntqModel.setDescription('Netasq Firewall model ')
ntqVersion = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVersion.setStatus('current')
if mibBuilder.loadTexts: ntqVersion.setDescription('Netasq Firewal version')
ntqSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ntqSerialNumber.setDescription('Netasq Firewall serial number')
ntqSystemName = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqSystemName.setStatus('current')
if mibBuilder.loadTexts: ntqSystemName.setDescription('Netasq Firewall system Name')
ntqSystemLanguage = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqSystemLanguage.setStatus('current')
if mibBuilder.loadTexts: ntqSystemLanguage.setDescription('Firewall language')
ntqNbEther = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqNbEther.setStatus('current')
if mibBuilder.loadTexts: ntqNbEther.setDescription('Number of ethernet interface')
ntqNbVlan = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqNbVlan.setStatus('current')
if mibBuilder.loadTexts: ntqNbVlan.setDescription('Number of VLAN interface')
ntqNbDialup = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqNbDialup.setStatus('current')
if mibBuilder.loadTexts: ntqNbDialup.setDescription('Number of Dialup')
ntqNbPPTP = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqNbPPTP.setStatus('current')
if mibBuilder.loadTexts: ntqNbPPTP.setDescription('Number of PPTP')
ntqNbSerial = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqNbSerial.setStatus('current')
if mibBuilder.loadTexts: ntqNbSerial.setDescription('Number of serial port')
ntqNbLoopback = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqNbLoopback.setStatus('current')
if mibBuilder.loadTexts: ntqNbLoopback.setDescription('Number of loopback interface')
ntqWatchdog = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqWatchdog.setStatus('current')
if mibBuilder.loadTexts: ntqWatchdog.setDescription('Watchdog')
ntqLed = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqLed.setStatus('current')
if mibBuilder.loadTexts: ntqLed.setDescription('Firewall Led')
ntqClone = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqClone.setStatus('current')
if mibBuilder.loadTexts: ntqClone.setDescription('Firewall Led')
ntqHADialup = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqHADialup.setStatus('current')
if mibBuilder.loadTexts: ntqHADialup.setDescription('Firewall Led')
mibBuilder.exportSymbols("NETASQ-PROPERTY-MIB", ntqNbDialup=ntqNbDialup, ntqSerialNumber=ntqSerialNumber, ntqSystemLanguage=ntqSystemLanguage, ntqVersion=ntqVersion, ntqLed=ntqLed, ntqHADialup=ntqHADialup, ntqNbSerial=ntqNbSerial, ntqNbPPTP=ntqNbPPTP, ntqModel=ntqModel, ntqClone=ntqClone, ntqNbVlan=ntqNbVlan, ntqNbEther=ntqNbEther, ntqSystemName=ntqSystemName, ntqNbLoopback=ntqNbLoopback, ntqWatchdog=ntqWatchdog)
