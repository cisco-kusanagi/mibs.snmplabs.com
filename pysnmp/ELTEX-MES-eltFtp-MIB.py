#
# PySNMP MIB module ELTEX-MES-eltFtp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-eltFtp-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
eltMesFtp, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesFtp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Unsigned32, Gauge32, Counter32, IpAddress, iso, TimeTicks, Counter64, MibIdentifier, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Unsigned32", "Gauge32", "Counter32", "IpAddress", "iso", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltFtpServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltFtpServerEnable.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-eltFtp-MIB", eltFtpServerEnable=eltFtpServerEnable)
