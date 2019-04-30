#
# PySNMP MIB module NMS-EPON-OLT-MAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-OLT-MAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Bits, Integer32, Counter32, TimeTicks, Gauge32, Counter64, Unsigned32, IpAddress, ObjectIdentity, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Bits", "Integer32", "Counter32", "TimeTicks", "Gauge32", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmsEponOltMat = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200))
oltFtpServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltFtpServerIpAddr.setStatus('mandatory')
oltFtpServerPort = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltFtpServerPort.setStatus('mandatory')
oltMatInsideIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltMatInsideIpAddr.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-OLT-MAT-MIB", oltFtpServerPort=oltFtpServerPort, oltMatInsideIpAddr=oltMatInsideIpAddr, oltFtpServerIpAddr=oltFtpServerIpAddr, nmsEponOltMat=nmsEponOltMat)
