#
# PySNMP MIB module ASCEND-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
firewallGroup, DisplayString = mibBuilder.importSymbols("ASCEND-MIB", "firewallGroup", "DisplayString")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, TimeTicks, Integer32, iso, IpAddress, Counter64, ObjectIdentity, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "TimeTicks", "Integer32", "iso", "IpAddress", "Counter64", "ObjectIdentity", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
firewallStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 16, 1))
firewallControl = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 16, 2))
fwallCtrlRuleName = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlRuleName.setStatus('mandatory')
fwallCtrlExecute = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-op", 1), ("enb-rule", 2), ("dis-rule", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExecute.setStatus('mandatory')
fwallCtrlTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlTimeOut.setStatus('mandatory')
fwallCtrlExtAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtAddr.setStatus('mandatory')
fwallCtrlExtAddrMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtAddrMask.setStatus('mandatory')
fwallCtrlExtPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtPort.setStatus('mandatory')
fwallCtrlExtPortMax = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtPortMax.setStatus('mandatory')
fwallCtrlIntAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntAddr.setStatus('mandatory')
fwallCtrlIntAddrMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntAddrMask.setStatus('mandatory')
fwallCtrlIntPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntPort.setStatus('mandatory')
fwallCtrlIntPortMax = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntPortMax.setStatus('mandatory')
fwallCtrlRoutAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlRoutAddr.setStatus('mandatory')
fwallCtrlAddrOpts = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlAddrOpts.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-FIREWALL-MIB", fwallCtrlExtAddr=fwallCtrlExtAddr, fwallCtrlExtPort=fwallCtrlExtPort, fwallCtrlIntAddr=fwallCtrlIntAddr, fwallCtrlExecute=fwallCtrlExecute, fwallCtrlIntPort=fwallCtrlIntPort, fwallCtrlIntAddrMask=fwallCtrlIntAddrMask, firewallStatus=firewallStatus, fwallCtrlExtAddrMask=fwallCtrlExtAddrMask, fwallCtrlTimeOut=fwallCtrlTimeOut, fwallCtrlRuleName=fwallCtrlRuleName, fwallCtrlRoutAddr=fwallCtrlRoutAddr, fwallCtrlExtPortMax=fwallCtrlExtPortMax, firewallControl=firewallControl, fwallCtrlAddrOpts=fwallCtrlAddrOpts, fwallCtrlIntPortMax=fwallCtrlIntPortMax)
