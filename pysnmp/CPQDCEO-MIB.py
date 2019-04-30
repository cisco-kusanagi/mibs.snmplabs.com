#
# PySNMP MIB module CPQDCEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQDCEO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
compaq, = mibBuilder.importSymbols("CPQHOST-MIB", "compaq")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysContact, sysName, sysDescr, sysLocation = mibBuilder.importSymbols("SNMPv2-MIB", "sysContact", "sysName", "sysDescr", "sysLocation")
Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Integer32, ObjectIdentity, NotificationType, NotificationType, MibIdentifier, Bits, Counter32, IpAddress, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Integer32", "ObjectIdentity", "NotificationType", "NotificationType", "MibIdentifier", "Bits", "Counter32", "IpAddress", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cpqDceo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 173))
environmentalDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 173, 1))
dceoTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 173, 1, 1))
trapDescription = MibScalar((1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDescription.setStatus('mandatory')
trapDeviceDetails = MibScalar((1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDeviceDetails.setStatus('mandatory')
trapDeviceMgmtUrl = MibScalar((1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDeviceMgmtUrl.setStatus('mandatory')
trapDceoHighPriority = NotificationType((1, 3, 6, 1, 4, 1, 232, 173) + (0,1)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQDCEO-MIB", "trapDescription"), ("CPQDCEO-MIB", "trapDeviceDetails"), ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
trapDceoMediumPriority = NotificationType((1, 3, 6, 1, 4, 1, 232, 173) + (0,2)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQDCEO-MIB", "trapDescription"), ("CPQDCEO-MIB", "trapDeviceDetails"), ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
trapDceoLowPriority = NotificationType((1, 3, 6, 1, 4, 1, 232, 173) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQDCEO-MIB", "trapDescription"), ("CPQDCEO-MIB", "trapDeviceDetails"), ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
mibBuilder.exportSymbols("CPQDCEO-MIB", trapDescription=trapDescription, cpqDceo=cpqDceo, trapDceoMediumPriority=trapDceoMediumPriority, trapDeviceDetails=trapDeviceDetails, environmentalDevice=environmentalDevice, dceoTrapInfo=dceoTrapInfo, trapDceoHighPriority=trapDceoHighPriority, trapDceoLowPriority=trapDceoLowPriority, trapDeviceMgmtUrl=trapDeviceMgmtUrl)
