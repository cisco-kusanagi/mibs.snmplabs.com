#
# PySNMP MIB module MIB-Dell-OME (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIB-Dell-OME
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ObjectIdentity, Integer32, iso, Counter32, ModuleIdentity, enterprises, NotificationType, Unsigned32, Counter64, MibIdentifier, TimeTicks, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ObjectIdentity", "Integer32", "iso", "Counter32", "ModuleIdentity", "enterprises", "NotificationType", "Unsigned32", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
enterpriseSW = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000))
sysMgmtBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 1000))
omEssentialsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100))
omEssentialsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1))
class DellString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 512)

class DellString1(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 128)

omeAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 1), DellString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertMessage.setStatus('mandatory')
omeAlertDevice = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 2), DellString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertDevice.setStatus('mandatory')
omeAlertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 3), DellString1()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertSeverity.setStatus('mandatory')
omeTestAlert = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,1)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertSeverity"))
omeAlertSystemUp = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,1000)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"))
omeAlertSystemDown = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,1001)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"))
omeAlertForwardedAlert = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,2000)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertSeverity"))
omeAlertUnknownStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3001)).setObjects(("MIB-Dell-OME", "omeAlertDevice"))
omeAlertNormalStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3002)).setObjects(("MIB-Dell-OME", "omeAlertDevice"))
omeAlertWarningStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3003)).setObjects(("MIB-Dell-OME", "omeAlertDevice"))
omeAlertCriticalStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3004)).setObjects(("MIB-Dell-OME", "omeAlertDevice"))
mibBuilder.exportSymbols("MIB-Dell-OME", omeAlertCriticalStatus=omeAlertCriticalStatus, omeAlertSystemDown=omeAlertSystemDown, sysMgmtBranch=sysMgmtBranch, omeAlertUnknownStatus=omeAlertUnknownStatus, DellString=DellString, omeAlertMessage=omeAlertMessage, omeAlertDevice=omeAlertDevice, omeTestAlert=omeTestAlert, omeAlertSystemUp=omeAlertSystemUp, omeAlertWarningStatus=omeAlertWarningStatus, omEssentialsMIB=omEssentialsMIB, dell=dell, DellString1=DellString1, enterpriseSW=enterpriseSW, omeAlertSeverity=omeAlertSeverity, omEssentialsTrap=omEssentialsTrap, omeAlertNormalStatus=omeAlertNormalStatus, omeAlertForwardedAlert=omeAlertForwardedAlert)
