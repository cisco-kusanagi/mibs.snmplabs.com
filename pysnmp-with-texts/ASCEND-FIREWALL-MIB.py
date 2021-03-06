#
# PySNMP MIB module ASCEND-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
firewallGroup, DisplayString = mibBuilder.importSymbols("ASCEND-MIB", "firewallGroup", "DisplayString")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Bits, Counter64, TimeTicks, iso, NotificationType, IpAddress, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Bits", "Counter64", "TimeTicks", "iso", "NotificationType", "IpAddress", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
firewallStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 16, 1))
firewallControl = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 16, 2))
fwallCtrlRuleName = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlRuleName.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlRuleName.setDescription('The name of the firewall rule to be enabled or disabled. This name corresponds with a name established when the firewall was created (as by the Secure Access Manager). There is no valid default value.')
fwallCtrlExecute = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-op", 1), ("enb-rule", 2), ("dis-rule", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExecute.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlExecute.setDescription('Cause a firewall given by the above parameters to be affected as requested. enb-rule causes a dynamic rule to be created; dis-rule causes a dynamic rule to cease operating. Default to 1 (no-op).')
fwallCtrlTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlTimeOut.setDescription('Time, expressed in seconds, during which this firewall rule will effect the firewall. After the expiration time, the rule will cease being effective exactly as if a del-rule (see fwallCtrlExecute above) had been executed on it. Default is defined in the firewall as defined by the firewall designer, and if none is given in the firewall, it is 3600 seconds.')
fwallCtrlExtAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtAddr.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlExtAddr.setDescription("Address of entity outside firewall. This value defaults to 0.0.0.0, equivalent to a don't care. May be used when selecting firewall to be updated (see fwallCtrlRoutAddr). The default value of zero could match any real IP address if ExtAddrMask is zero, otherwise it would match NO IP address.")
fwallCtrlExtAddrMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtAddrMask.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlExtAddrMask.setDescription('Netmask of entity outside firewall. This value defaults to 255.255.255.255, equivalent to a host address if fwallCtrlExtAddr is non-zero.')
fwallCtrlExtPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtPort.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlExtPort.setDescription("For external entity, specifies a port number. Defaults to 0, equivalent to don't care.")
fwallCtrlExtPortMax = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlExtPortMax.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlExtPortMax.setDescription('For external entity, specifies the maximum port number of a range of ports. Defaults to 0, equivalent to specifying a single port number if fwallCtrlExtPort is nonzero.')
fwallCtrlIntAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntAddr.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlIntAddr.setDescription("Address of entity inside firewall. This value defaults to 0.0.0.0, equivalent to a don't care.")
fwallCtrlIntAddrMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntAddrMask.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlIntAddrMask.setDescription('Netmask of entity inside firewall. This value defaults to 255.255.255.255, equivalent to a host address if fwallCtrlIntAddr is non-zero.')
fwallCtrlIntPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntPort.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlIntPort.setDescription("For Internal entity, specifies a port number. Defaults to 0, equivalent to don't care.")
fwallCtrlIntPortMax = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlIntPortMax.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlIntPortMax.setDescription('For Internal entity, specifies the maximum port number of a range of ports. Defaults to 0, equivalent to specifying a single port number if fwallCtrlIntPort is nonzero.')
fwallCtrlRoutAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlRoutAddr.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlRoutAddr.setDescription('This address may be supplied by the management station to choose a firewall for alteration. The default for this address is 0.0.0.0, which would cause the router to use fwallCtrlExtAddr to choose its firewall instead.')
fwallCtrlAddrOpts = MibScalar((1, 3, 6, 1, 4, 1, 529, 16, 2, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallCtrlAddrOpts.setStatus('mandatory')
if mibBuilder.loadTexts: fwallCtrlAddrOpts.setDescription("Firewall requests may require additional bit- encoded options to determine the firewall's new behavior. This options variable is a mechanism to allow those options to be defined at a later date. Until then, this variable really has no meaning.")
mibBuilder.exportSymbols("ASCEND-FIREWALL-MIB", fwallCtrlExtAddr=fwallCtrlExtAddr, fwallCtrlExecute=fwallCtrlExecute, fwallCtrlTimeOut=fwallCtrlTimeOut, fwallCtrlExtPort=fwallCtrlExtPort, fwallCtrlIntAddr=fwallCtrlIntAddr, fwallCtrlRoutAddr=fwallCtrlRoutAddr, fwallCtrlIntPort=fwallCtrlIntPort, fwallCtrlRuleName=fwallCtrlRuleName, fwallCtrlExtPortMax=fwallCtrlExtPortMax, firewallStatus=firewallStatus, fwallCtrlExtAddrMask=fwallCtrlExtAddrMask, fwallCtrlIntAddrMask=fwallCtrlIntAddrMask, fwallCtrlIntPortMax=fwallCtrlIntPortMax, fwallCtrlAddrOpts=fwallCtrlAddrOpts, firewallControl=firewallControl)
