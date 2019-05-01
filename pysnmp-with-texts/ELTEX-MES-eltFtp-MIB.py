#
# PySNMP MIB module ELTEX-MES-eltFtp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-eltFtp-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
eltMesFtp, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesFtp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, MibIdentifier, Counter32, TimeTicks, NotificationType, IpAddress, Bits, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "MibIdentifier", "Counter32", "TimeTicks", "NotificationType", "IpAddress", "Bits", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Integer32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltFtpServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltFtpServerEnable.setStatus('current')
if mibBuilder.loadTexts: eltFtpServerEnable.setDescription('Enable and disable FTP server.')
mibBuilder.exportSymbols("ELTEX-MES-eltFtp-MIB", eltFtpServerEnable=eltFtpServerEnable)
