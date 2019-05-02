#
# PySNMP MIB module UMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UMS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, Gauge32, Bits, Unsigned32, iso, TimeTicks, Counter64, NotificationType, ObjectIdentity, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "Unsigned32", "iso", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("UMS-MIB", String=String, ibmpsgEvent=ibmpsgEvent, win32WMI=win32WMI, ibmpsgSMART=ibmpsgSMART, umservices=umservices, ibmpsg=ibmpsg, win32SMBIOS=win32SMBIOS, Sint64=Sint64, ibmpsgITDirector=ibmpsgITDirector, Uint32=Uint32, ibmpsgAgent=ibmpsgAgent, cimv2=cimv2, ibmpsgVitalProductData=ibmpsgVitalProductData, Uint16=Uint16, Sint32=Sint32, Real64=Real64, ibm=ibm, Datetime=Datetime, Boolean=Boolean, Uint64=Uint64, ibmpsgLMSensor=ibmpsgLMSensor, ibmpsgEventSubsystem=ibmpsgEventSubsystem, win32Event=win32Event, ibmpsgAssetID=ibmpsgAssetID, ibmProd=ibmProd, Uint8=Uint8, Sint16=Sint16, ibmpsgAlertOnLAN=ibmpsgAlertOnLAN, win32=win32, ibmpsgHealth=ibmpsgHealth, Sint8=Sint8, Real32=Real32)
