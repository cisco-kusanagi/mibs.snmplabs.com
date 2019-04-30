#
# PySNMP MIB module UMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UMS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, ModuleIdentity, Unsigned32, MibIdentifier, Gauge32, Counter32, enterprises, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "Counter32", "enterprises", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
umservices = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159))
cimv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1))
ibmpsg = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1))
ibmpsgEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 0))
ibmpsgAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 10))
ibmpsgEventSubsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 20))
ibmpsgHealth = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 30))
ibmpsgVitalProductData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 40))
ibmpsgSMART = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 50))
ibmpsgAssetID = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60))
ibmpsgAlertOnLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70))
ibmpsgLMSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80))
ibmpsgITDirector = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 90))
win32 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2))
win32Event = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 0))
win32WMI = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10))
win32SMBIOS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 20))
class Boolean(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1)

class Uint8(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class Sint8(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class Uint16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Sint16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32767, 32766)

class Uint32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Sint32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483647, 2147483646)

class Uint64(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1)

class Sint64(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1)

class Real32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1)

class Real64(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1)

class String(OctetString):
    pass

class Datetime(OctetString):
    pass

mibBuilder.exportSymbols("UMS-MIB", ibm=ibm, String=String, Real64=Real64, umservices=umservices, ibmpsgEvent=ibmpsgEvent, Sint8=Sint8, Sint32=Sint32, ibmpsgHealth=ibmpsgHealth, ibmpsgITDirector=ibmpsgITDirector, win32SMBIOS=win32SMBIOS, Uint8=Uint8, Uint32=Uint32, Boolean=Boolean, ibmpsgVitalProductData=ibmpsgVitalProductData, ibmpsgEventSubsystem=ibmpsgEventSubsystem, Uint64=Uint64, Uint16=Uint16, win32=win32, ibmpsgAlertOnLAN=ibmpsgAlertOnLAN, ibmpsgAgent=ibmpsgAgent, win32WMI=win32WMI, ibmProd=ibmProd, Sint16=Sint16, Datetime=Datetime, Sint64=Sint64, Real32=Real32, ibmpsgLMSensor=ibmpsgLMSensor, cimv2=cimv2, ibmpsgAssetID=ibmpsgAssetID, ibmpsgSMART=ibmpsgSMART, win32Event=win32Event, ibmpsg=ibmpsg)
