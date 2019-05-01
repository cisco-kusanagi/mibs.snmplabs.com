#
# PySNMP MIB module NMS-EPON-OLT-MAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-OLT-MAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:21:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Gauge32, Counter64, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Integer32, ModuleIdentity, ObjectIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Gauge32", "Counter64", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmsEponOltMat = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200))
oltFtpServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltFtpServerIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: oltFtpServerIpAddr.setDescription('FTP server IP address for HS update. Use only for BSTAR 85 series.')
oltFtpServerPort = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltFtpServerPort.setStatus('mandatory')
if mibBuilder.loadTexts: oltFtpServerPort.setDescription('FTP server port for HS update. Use only for BSTAR 85 series.')
oltMatInsideIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 200, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltMatInsideIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: oltMatInsideIpAddr.setDescription('Mat inside interface IP address. Use only for BSTAR 85 series.')
mibBuilder.exportSymbols("NMS-EPON-OLT-MAT-MIB", oltFtpServerIpAddr=oltFtpServerIpAddr, nmsEponOltMat=nmsEponOltMat, oltMatInsideIpAddr=oltMatInsideIpAddr, oltFtpServerPort=oltFtpServerPort)
